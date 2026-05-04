@echo off
echo ========================================
echo     Setting up ShelBot Lite...
echo ========================================

echo.
echo Checking for Python...
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Python was NOT found in your PATH!
    echo.
    echo Please run this command in a new PowerShell or CMD window:
    echo python --version
    echo.
    echo If that doesn't work, we need to fix your Python installation/PATH.
    echo.
    pause
    exit
) else (
    echo ✅ Python found!
    python --version
)

echo.
echo Creating virtual environment...
python -m venv venv

call venv\Scripts\activate
pip install -r requirements.txt

echo.
echo ✅ Setup complete!
echo.
echo You can now run 'run.bat'
pause