@echo off
cd /d "%~dp0.."
echo Starting MediSync Outbound Workspace...
echo.
echo Open in browser: http://localhost:8080
echo.
echo Press Ctrl+C to stop.
echo.
npx -y serve -p 8080
