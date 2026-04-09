# Pillow Installation Guide for Windows

## Method 1: Using Python's built-in pip (Recommended)

### Step 1: Check Python Installation
Open Command Prompt or PowerShell and run:
```cmd
python --version
```
If you see "Python 3.x.x", continue to Step 2.

If Python is not found, download from: https://python.org/downloads/

### Step 2: Install Pillow
```cmd
python -m pip install pillow
```

## Method 2: Using pip directly (if Method 1 fails)

### Option A: Use full pip path
```cmd
C:\Python311\Scripts\pip.exe install pillow
```
*(Replace `311` with your Python version)*

### Option B: Add pip to PATH
1. Find your Python installation folder (usually `C:\Python311\` or similar)
2. Add `C:\Python311\Scripts\` to your system PATH
3. Restart Command Prompt
4. Run: `pip install pillow`

## Method 3: Using Python executable directly

### Download and install manually:
1. Download Pillow wheel from: https://pypi.org/project/Pillow/#files
2. Choose the correct version for your Python (cp311 for Python 3.11)
3. Install with: `python -m pip install Pillow-10.2.0-cp311-cp311-win_amd64.whl`

## Method 4: Using Anaconda/Miniconda (if installed)

```cmd
conda install pillow
```

## Method 5: Using Chocolatey (if installed)

```cmd
choco install python-pillow
```

## Troubleshooting

### "python is not recognized"
- Install Python from https://python.org
- Make sure to check "Add Python to PATH" during installation

### "pip is not recognized"
- Use `python -m pip` instead of `pip`
- Or add Python Scripts folder to PATH

### Permission errors
- Run Command Prompt as Administrator
- Or use: `python -m pip install --user pillow`

## Verification

After installation, verify with:
```python
python -c "from PIL import Image; print('Pillow installed successfully!')"
```

## Alternative: Pre-built Executable

If all else fails, I've created a standalone enhancement script that doesn't require external dependencies. Let me know if you need this version.