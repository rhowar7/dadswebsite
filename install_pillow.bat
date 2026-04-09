@echo off
echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo Python not found. Please install Python from https://python.org
    pause
    exit /b 1
)

echo.
echo Installing Pillow...
python -m pip install pillow

if %errorlevel% equ 0 (
    echo.
    echo Pillow installed successfully!
    echo.
    echo Verifying installation...
    python -c "from PIL import Image; print('Pillow is working!')"
) else (
    echo.
    echo Installation failed. Trying alternative method...
    python -m pip install --user pillow
)

echo.
echo Press any key to continue...
pause >nul