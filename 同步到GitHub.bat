@echo off
cls

echo ========================================
echo   Starting MD Portfolio Sync...
echo ========================================

:: 1. Go to current directory
cd /d "%~dp0"

:: 2. Track all changes
echo [1/3] Scanning for file changes...
git add .

:: 3. Commit with timestamp
set msg=Auto-update: %date% %time%
echo [2/3] Creating commit snapshot...
git commit -m "%msg%"

:: 4. Push to GitHub
echo [3/3] Pushing to GitHub cloud...
git push origin main

echo.
echo ========================================
echo   Success! GitHub repository updated.
echo ========================================
echo.
pause