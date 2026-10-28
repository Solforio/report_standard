param(
  [Parameter(Mandatory=$true)][ValidateSet('word','ppt')][string]$Mode,
  [Parameter(Mandatory=$true)][string]$In,
  [string]$Pdf = '',
  [switch]$UpdateFields
)
# Actualiza índice/campos de un DOCX y/o exporta a PDF usando Word o PowerPoint instalados.
$ErrorActionPreference = 'Stop'
if ($Mode -eq 'word') {
  $app = New-Object -ComObject Word.Application
  $app.Visible = $false; $app.DisplayAlerts = 0
  try {
    $doc = $app.Documents.Open($In, $false, $false)
    if ($UpdateFields) {
      $doc.Repaginate()
      foreach ($t in $doc.TablesOfContents) { $t.Update() }
      $doc.Fields.Update() | Out-Null
      foreach ($t in $doc.TablesOfContents) { $t.Update() }
      $doc.Save()
    }
    if ($Pdf) { $doc.ExportAsFixedFormat($Pdf, 17) }
    $doc.Close(0)
  } finally { $app.Quit() }
} else {
  $app = New-Object -ComObject PowerPoint.Application
  try {
    $app.DisplayAlerts = 1  # ppAlertsNone: sin diálogos modales (si no, Close puede quedarse colgado)
    $p = $app.Presentations.Open($In, $true, $false, $false)
    if ($Pdf) { $p.SaveAs($Pdf, 32) }
    try { $p.Close() } catch { }
  } finally { try { $app.Quit() } catch { } }
}
'ok'
