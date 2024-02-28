@echo off
setlocal enabledelayedexpansion

echo =================================
echo ICT Inventory System TeXParser
echo Batch Script for TeX Dependencies
echo Version 1.2 - 2024/02/17
echo =================================
echo.

@echo off

for /f "tokens=1-4 delims=/ " %%i in ("!date!") do (
     set dow=%%i
     set month=%%j
     set day=%%k
     set year=%%l
)

set currDate=!year!-!month!-!day!
set texliveDate=!year!!month!!day!

set TEXLIVE_INSTALL_DIR=C:\texlive
set TEXLIVE_ZIP=install-tl.zip
set TEXLIVE_EXT=install-tl-!texliveDate!

echo --- SYSTEM CHECK ---
REM Check if TeX Live is installed
echo [!currDate! !TIME!]: Checking installation of TeX Live in !TEXLIVE_INSTALL_DIR!
if exist "!TEXLIVE_INSTALL_DIR!" (
    echo [!currDate! !TIME!]: TeX Live is already installed.
    goto :end
) else (
    echo [!currDate! !TIME!]: TeX Live is not installed.
)

echo [!currDate! !TIME!]: Checking !TEXLIVE_ZIP!
REM Check if install-tl.zip already exists
if not exist "!TEXLIVE_ZIP!" (
    REM Download the TeX Live package manager
    echo [!currDate! !TIME!]: Downloading files for TeX Live...

    powershell -Command "& {Invoke-WebRequest -Uri http://mirror.ctan.org/systems/texlive/tlnet/!TEXLIVE_ZIP! -OutFile !TEXLIVE_ZIP!}"

    echo [!currDate! !TIME!]: !TEXLIVE_ZIP! has been downloaded successfully.
) else (
	echo [!currDate! !TIME!]: !TEXLIVE_ZIP! already exists.
)

REM Unzip the downloaded file
powershell Expand-Archive -Path .\!TEXLIVE_ZIP! -DestinationPath .

if not exist "!TEXLIVE_EXT!" (
    echo [!currDate! !TIME!]: Currently unzipped install-tl-YYYYMMDD does not match latest build. 
    echo.
    set /p TEXLIVE_EXT=Please manually enter directory name: 
    if not exist "!TEXLIVE_EXT!" goto :err
)

echo.

echo --- INSTALLATION ---
REM Prompt the user before proceeding
echo Disk Space Required: 436 MB
set /p continue=Installation will now proceed. Do you want to continue? (y/n): 
if /i "!continue!" neq "y" goto :end
echo.
echo [!currDate! !TIME!]: Launching install-tl...

REM Copy texlive profile
copy "./texlive.profile" "./!TEXLIVE_EXT!"

cd !TEXLIVE_EXT!

REM Launch install-tl-windows with pre-defined profile
start install-tl-windows -profile texlive.profile
goto :end

:err
echo.
echo DirectoryNameError: Directory not found.
echo.
pause

:end
