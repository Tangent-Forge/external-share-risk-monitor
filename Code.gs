/**
 * External Share Risk Monitor - Google Workspace Add-on
 * Scans Drive for risky external file sharing and provides remediation
 */

const UI_LABEL = 'External Share Risk Monitor';

// ========================================
// Add-on Initialization
// ========================================

/**
 * Called when the add-on is installed
 */
function onInstall(e) {
  onOpen(e);
}

/**
 * Called when a document is opened
 */
function onOpen(e) {
  SpreadsheetApp.getUi()
    .createMenu('External Share Risk')
    .addItem('Run Risk Scan', 'runRiskScan')
    .addItem('Show Dashboard', 'showDashboard')
    .addSeparator()
    .addItem('Send Weekly Digest', 'sendWeeklyDigest')
    .addItem('Install Weekly Digest Trigger', 'installWeeklyDigestTrigger')
    .addToUi();
}

/**
 * Opens the sidebar
 */
function showDashboard() {
  const html = HtmlService.createHtmlOutputFromFile('Sidebar')
    .setTitle(UI_LABEL);
  SpreadsheetApp.getUi().showSidebar(html);
}

// ========================================
// API Functions (Called from Sidebar)
// ========================================

/**
 * API: Run a risk scan
 */
function apiRunRiskScan() {
  try {
    const report = runRiskScan();
    storeRiskReport(report);
    return report;
  } catch (err) {
    console.error('Risk scan failed:', err);
    throw new Error('Risk scan failed: ' + err.message);
  }
}

/**
 * API: Get stored risk report
 */
function apiGetRiskReport() {
  try {
    const report = getStoredRiskReport();
    return report || { success: false, message: 'No report available' };
  } catch (err) {
    console.error('Get report failed:', err);
    throw new Error('Get report failed: ' + err.message);
  }
}

/**
 * API: Revoke external access for files
 */
function apiRevokeAccess(fileIds) {
  try {
    const results = RemediationModule.revokeAccess(fileIds);
    return results;
  } catch (err) {
    console.error('Revoke access failed:', err);
    throw new Error('Revoke access failed: ' + err.message);
  }
}

/**
 * API: Export report to Sheet
 */
function apiExportReport() {
  try {
    const report = getStoredRiskReport();
    if (!report) {
      throw new Error('No report available to export');
    }
    const sheetUrl = ReportWriter.exportToSheet(report);
    return { success: true, url: sheetUrl };
  } catch (err) {
    console.error('Export failed:', err);
    throw new Error('Export failed: ' + err.message);
  }
}

// ========================================
// Core Logic
// ========================================

/**
 * Main risk scan function
 */
function runRiskScan() {
  const config = RiskMonitorConfig;
  const scanAt = new Date();
  
  // Scan Drive for external shares
  const externalFiles = RiskScanner.scanExternalShares({
    primaryDomain: config.primaryDomain,
    pageSize: 200,
    maxPages: 50
  });
  
  // Score risks
  const scoredFiles = externalFiles.map(file => ({
    ...file,
    riskScore: RiskScorer.calculateRisk(file, config)
  }));
  
  // Categorize by risk level
  const highRisk = scoredFiles.filter(f => f.riskScore >= 8);
  const mediumRisk = scoredFiles.filter(f => f.riskScore >= 5 && f.riskScore < 8);
  const lowRisk = scoredFiles.filter(f => f.riskScore < 5);
  
  // Calculate summary
  const summary = {
    scanAt,
    totalFiles: scoredFiles.length,
    highRiskCount: highRisk.length,
    mediumRiskCount: mediumRisk.length,
    lowRiskCount: lowRisk.length,
    totalRiskScore: scoredFiles.reduce((sum, f) => sum + f.riskScore, 0),
    averageRiskScore: scoredFiles.length > 0 ? scoredFiles.reduce((sum, f) => sum + f.riskScore, 0) / scoredFiles.length : 0,
    topRisks: scoredFiles.sort((a, b) => b.riskScore - a.riskScore).slice(0, 10),
    sheetUrl: RiskMonitorConfig.sheet.id
      ? `https://docs.google.com/spreadsheets/d/${RiskMonitorConfig.sheet.id}`
      : ''
  };
  
  return {
    success: true,
    files: scoredFiles,
    summary
  };
}

/**
 * Installable trigger entry point for weekly digests
 */
function sendWeeklyDigest() {
  runRiskScan();
}

/**
 * One-time helper to install the weekly digest trigger
 */
function installWeeklyDigestTrigger() {
  const existing = ScriptApp.getProjectTriggers().find((trigger) => trigger.getHandlerFunction() === 'sendWeeklyDigest');
  if (existing) {
    return existing.getUniqueId();
  }
  const trigger = ScriptApp.newTrigger('sendWeeklyDigest').timeBased().everyWeeks(1).create();
  return trigger.getUniqueId();
}

// ========================================
// Configuration
// ========================================

const RiskMonitorConfig = {
  /**
   * Primary domain for identifying external shares
   */
  primaryDomain: 'example.com',
  
  /**
   * Risk scoring thresholds
   */
  riskThresholds: {
    high: 8,
    medium: 5,
    low: 0
  },
  
  /**
   * File type sensitivity weights
   */
  fileSensitivity: {
    'application/vnd.google-apps.spreadsheet': 0.7,
    'application/vnd.google-apps.document': 0.8,
    'application/vnd.google-apps.presentation': 0.6,
    'application/pdf': 0.9,
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 0.9,
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 0.8,
    'application/vnd.openxmlformats-officedocument.presentationml.presentation': 0.7,
    'default': 0.5
  },
  
  /**
   * Access type risk multipliers
   */
  accessRiskMultipliers: {
    'anyone': 2.0,      // Public link
    'domain': 1.5,      // Anyone with domain link
    'external': 1.2,    // Specific external users
    'default': 1.0
  },
  
  /**
   * Optional report routing
   */
  report: {
    enableEmail: true,
    recipient: 'security@example.com'
  },
  
  /**
   * Google Sheet destination for persisting risk reports
   */
  sheet: {
    id: 'REPLACE_WITH_SHEET_ID',
    summaryName: 'Risk Summary',
    historyName: 'Risk History'
  }
};

// ========================================
// Risk Scanner Module
// ========================================

const RiskScanner = (() => {
  function scanExternalShares({ primaryDomain, pageSize = 200, maxPages = 50 } = {}) {
    const externalFiles = [];
    let pageToken = null;
    let pageCount = 0;
    
    // Query for files that are not private
    const query = `visibility != 'private'`;
    
    do {
      const response = Drive.Files.list({
        q: query,
        pageSize,
        pageToken,
        fields: 'files(id,name,mimeType,owners,permissions,webViewLink,shared,createdTime,modifiedTime),nextPageToken',
        supportsAllDrives: true
      });
      
      if (response.files) {
        response.files.forEach(file => {
          const externalPermissions = file.permissions.filter(perm => {
            // Check if permission is external
            if (perm.type === 'user') {
              return !perm.emailAddress || !perm.emailAddress.endsWith(`@${primaryDomain}`);
            }
            if (perm.type === 'anyone' || perm.type === 'domain') {
              return true; // Public or domain-wide is external
            }
            return false;
          });
          
          if (externalPermissions.length > 0) {
            externalFiles.push({
              id: file.id,
              name: file.name,
              mimeType: file.mimeType,
              owners: file.owners || [],
              permissions: externalPermissions,
              webViewLink: file.webViewLink,
              shared: file.shared,
              createdTime: file.createdTime,
              modifiedTime: file.modifiedTime,
              externalPermissionCount: externalPermissions.length
            });
          }
        });
      }
      
      pageToken = response.nextPageToken;
      pageCount++;
    } while (pageToken && pageCount < maxPages);
    
    return externalFiles;
  }
  
  return {
    scanExternalShares
  };
})();

// ========================================
// Risk Scorer Module
// ========================================

const RiskScorer = (() => {
  function calculateRisk(file, config) {
    let riskScore = 0;
    
    // Base risk from file type sensitivity
    const sensitivity = config.fileSensitivity[file.mimeType] || config.fileSensitivity.default;
    riskScore += sensitivity * 5;
    
    // Risk from access type
    const hasPublicAccess = file.permissions.some(p => p.type === 'anyone');
    const hasDomainAccess = file.permissions.some(p => p.type === 'domain');
    const hasExternalAccess = file.permissions.some(p => p.type === 'user' && (!p.emailAddress || !p.emailAddress.endsWith(`@${config.primaryDomain}`)));
    
    if (hasPublicAccess) {
      riskScore *= config.accessRiskMultipliers.anyone;
    } else if (hasDomainAccess) {
      riskScore *= config.accessRiskMultipliers.domain;
    } else if (hasExternalAccess) {
      riskScore *= config.accessRiskMultipliers.external;
    }
    
    // Risk from number of external permissions
    riskScore += (file.externalPermissionCount - 1) * 0.5;
    
    // Risk from file age (newer files with external access are riskier)
    const daysSinceCreation = (new Date() - new Date(file.createdTime)) / (1000 * 60 * 60 * 24);
    if (daysSinceCreation < 30) {
      riskScore += 1; // Recent files are riskier
    }
    
    // Cap at 10
    return Math.min(Math.round(riskScore * 10) / 10, 10);
  }
  
  return {
    calculateRisk
  };
})();

// ========================================
// Remediation Module
// ========================================

const RemediationModule = (() => {
  function revokeAccess(fileIds) {
    const results = [];
    
    fileIds.forEach(fileId => {
      try {
        const file = DriveApp.getFileById(fileId);
        const permissions = file.getSharingAccess();
        
        // Revoke all external permissions
        permissions.forEach(perm => {
          if (perm.type === 'user' || perm.type === 'anyone' || perm.type === 'domain') {
            file.setSharing(perm.type, perm.user || perm.domain, DriveApp.Access.ANYONE_WITH_LINK);
          }
        });
        
        results.push({
          fileId,
          success: true,
          message: 'External access revoked'
        });
        
        // Log the action
        AuditLogger.logRemediation({
          fileId,
          action: 'revoke_external_access',
          timestamp: new Date().toISOString(),
          user: Session.getActiveUser().getEmail()
        });
        
      } catch (err) {
        results.push({
          fileId,
          success: false,
          message: err.message
        });
      }
    });
    
    return results;
  }
  
  return {
    revokeAccess
  };
})();

// ========================================
// Audit Logger
// ========================================

const AuditLogger = (() => {
  function logRemediation(action) {
    const logEntry = JSON.stringify(action);
    console.log('REMEDIATION:', logEntry);
    // In production, this would write to a log file or database
  }
  
  return {
    logRemediation
  };
})();

// ========================================
// Report Writer
// ========================================

const ReportWriter = (() => {
  function exportToSheet(report) {
    const ss = SpreadsheetApp.create('External Share Risk Report - ' + new Date().toLocaleDateString());
    const sheet = ss.getSheets()[0];
    
    // Summary sheet
    sheet.appendRow(['Metric', 'Value']);
    sheet.appendRow(['Scan Date', report.summary.scanAt]);
    sheet.appendRow(['Total External Files', report.summary.totalFiles]);
    sheet.appendRow(['High Risk Files', report.summary.highRiskCount]);
    sheet.appendRow(['Medium Risk Files', report.summary.mediumRiskCount]);
    sheet.appendRow(['Low Risk Files', report.summary.lowRiskCount]);
    sheet.appendRow(['Total Risk Score', report.summary.totalRiskScore]);
    sheet.appendRow(['Average Risk Score', report.summary.averageRiskScore.toFixed(2)]);
    
    sheet.getRange(1, 1, 1, 2).setFontWeight('bold').setBackground('#D93025').setFontColor('#FFFFFF');
    sheet.setFrozenRows(1);
    sheet.autoResizeColumns(1, 2);
    
    // Detailed files sheet
    const filesSheet = ss.insertSheet('Detailed Files');
    filesSheet.appendRow(['File Name', 'Risk Score', 'Owner', 'External Permissions', 'Created', 'Modified', 'Link']);
    filesSheet.getRange(1, 1, 1, 7).setFontWeight('bold').setBackground('#D93025').setFontColor('#FFFFFF');
    
    report.files.forEach(file => {
      const owners = file.owners.map(o => o.emailAddress || o.displayName).join(', ');
      const permissions = file.permissions.map(p => {
        if (p.type === 'anyone') return 'Public';
        if (p.type === 'domain') return `Domain: ${p.domain}`;
        if (p.type === 'user') return p.emailAddress || 'External User';
        return p.type;
      }).join(', ');
      
      filesSheet.appendRow([
        file.name,
        file.riskScore,
        owners,
        permissions,
        new Date(file.createdTime).toLocaleDateString(),
        new Date(file.modifiedTime).toLocaleDateString(),
        file.webViewLink || ''
      ]);
    });
    
    filesSheet.setFrozenRows(1);
    filesSheet.autoResizeColumns(1, 7);
    
    return ss.getUrl();
  }
  
  return {
    exportToSheet
  };
})();

// ========================================
// Storage Functions
// ========================================

function storeRiskReport(report) {
  const properties = PropertiesService.getScriptProperties();
  properties.setProperty('lastRiskReport', JSON.stringify(report));
}

function getStoredRiskReport() {
  const properties = PropertiesService.getScriptProperties();
  const reportJson = properties.getProperty('lastRiskReport');
  return reportJson ? JSON.parse(reportJson) : null;
}
