Set-Location (Split-Path $PSScriptRoot)

Write-Host "Starting MediSync Outbound Workspace..." -ForegroundColor Cyan
Write-Host ""
Write-Host "Open in browser: http://localhost:8080/workspace/" -ForegroundColor Green
Write-Host ""
Write-Host "Press Ctrl+C to stop." -ForegroundColor Yellow
Write-Host ""

python -m http.server 8080
