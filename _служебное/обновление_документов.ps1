# Скрипт обновления: повторная проверка/загрузка документов комплекта 6281 с bom.firpo.ru
# Использование:
#   powershell -ExecutionPolicy Bypass -File обновление_документов.ps1 [-Download]
# Без -Download — только список актуальных файлов и сверка с локальными.
param([switch]$Download)
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$dest = 'E:\демоэкзамен КИП'
$api  = 'https://bom.firpo.ru/api/EvaluationKit/GetPublicDocuments/6281'

$ua    = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36'
$json  = Invoke-RestMethod -Uri $api -Headers @{ 'User-Agent' = $ua }

$docs = $json.documentAttempts | Sort-Object id | ForEach-Object {
  [PSCustomObject]@{
    Id   = $_.id
    Name = $_.uploadedFile.originalName
    Link = ('https://bom.firpo.ru' + $_.publicDownloadLink)
    Approved = $_.approvedTime
  }
}

Write-Host '=== Документы комплекта 6281 (КИМ 15.01.31-1-2027) ==='
$docs | Format-Table Id, Name, Approved -AutoSize | Out-String -Width 120

foreach ($d in $docs) {
  $outPath = Join-Path $dest $d.Name
  if (Test-Path $outPath) {
    Write-Host ("есть на диске: " + $d.Name)
  } else {
    Write-Host ("НЕТ на диске: " + $d.Name)
  }
}

if ($Download.IsPresent) {
  foreach ($d in $docs) {
    $outPath = Join-Path $dest $d.Name
    if (-not (Test-Path $outPath)) {
      $encoded = [System.Uri]::EscapeUriString($d.Link)
      curl.exe -L --fail --retry 2 -A $ua -o $outPath $encoded
      Write-Host ("загружен: " + $d.Name)
    }
  }
  Write-Host 'Готово.'
} else {
  Write-Host 'Для загрузки недостающих файлов запустите с параметром -Download.'
}
