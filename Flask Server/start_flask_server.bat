@echo off
title Community - Flask Testserver
cd /d "%~dp0"

echo.
echo ================================================
echo   Community Flask Testserver
echo ================================================
echo.

py --version >nul 2>&1
if errorlevel 1 (
    echo Python wurde nicht gefunden.
    echo Bitte Python installieren und dabei "Add Python to PATH" aktivieren.
    pause
    exit /b 1
)

py -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo Flask ist noch nicht installiert.
    echo Flask wird jetzt installiert...
    py -m pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo Flask konnte nicht installiert werden.
        pause
        exit /b 1
    )
)

echo Starte Server...
py app.py
pause
