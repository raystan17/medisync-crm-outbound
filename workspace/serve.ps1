Set-Location (Split-Path $PSScriptRoot)

Write-Host "Starting MediSync Outbound Workspace..." -ForegroundColor Cyan
Write-Host ""
Write-Host "Open in browser: http://localhost:8080" -ForegroundColor Green
Write-Host ""
Write-Host "Press Ctrl+C to stop." -ForegroundColor Yellow
Write-Host ""

npx -y serve -p 8080
