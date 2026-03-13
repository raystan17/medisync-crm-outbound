@echo off
cd /d "%~dp0.."
echo Starting MediSync Outbound Workspace...
echo.
echo Open in browser: http://localhost:8080/workspace/
echo.
echo Press Ctrl+C to stop.
echo.
python -m http.server 8080
