param(
  [Parameter(Mandatory)][string]$Html,
  [Parameter(Mandatory)][string]$Docx,
  [string]$Pdf = "",
  [int]$TimeoutSec = 170
)
# Converts an HTML file to .docx (and optionally .pdf) through Word COM, with a watchdog:
# the COM work runs in a job; if it does not finish in time, the new WINWORD process is killed.
$before = @(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object Id)
$job = Start-Job -ScriptBlock {
  param($Html, $Docx, $Pdf)
  $m = [Type]::Missing
  $w = New-Object -ComObject Word.Application
  $w.Visible = $false
  $w.DisplayAlerts = 0          # wdAlertsNone
  $w.AutomationSecurity = 3     # msoAutomationSecurityForceDisable (no macro / protected-view prompts)
  $w.Options.ConfirmConversions = $false
  # Open(FileName, ConfirmConversions, ReadOnly, AddToRecentFiles, PasswordDocument, PasswordTemplate,
  #      Revert, WritePasswordDocument, WritePasswordTemplate, Format(7 = web pages), Encoding(65001 = UTF-8),
  #      Visible, OpenAndRepair, DocumentDirection, NoEncodingDialog)
  # Late-bound COM inside a job rejects [Type]::Missing, so use the 4-argument form only.
  $d = $w.Documents.Open($Html, $false, $true, $false)
  $d.SaveAs2($Docx, 16)         # wdFormatDocumentDefault (.docx)
  if ($Pdf) { $d.ExportAsFixedFormat($Pdf, 17) }   # wdExportFormatPDF
  $pages = $d.ComputeStatistics(2)
  $words = $d.ComputeStatistics(0)
  $d.Close($false)
  $w.Quit()
  "ok: $pages pages, $words words"
} -ArgumentList $Html, $Docx, $Pdf
if (Wait-Job $job -Timeout $TimeoutSec) { Receive-Job $job } else { "TIMEOUT after $TimeoutSec s"; Stop-Job $job }
Remove-Job $job -Force -ErrorAction SilentlyContinue
Get-Process WINWORD -ErrorAction SilentlyContinue | Where-Object { $before -notcontains $_.Id } | ForEach-Object {
  Stop-Process -Id $_.Id -Force; "killed leftover WINWORD $($_.Id)"
}
