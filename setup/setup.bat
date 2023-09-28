@ECHO OFF

REM Configures Python setup for project

REM Get the directory of the batch script
SET "SCRIPT_DIR=%~dp0"

REM Switch to batch dir, then to project root
CD %SCRIPT_DIR%\..

REM Check if venv exists
IF EXIST "venv" (
    ECHO Virtual environment already exists.
) ELSE (
    ECHO Creating virtual environment...
    python -m venv venv

    REM Check if venv creation was successful
    IF ERRORLEVEL 1 (
        ECHO Error: Virtual environment creation failed.
        GOTO :EOF  REM Exit the script
    ) ELSE (
        ECHO Virtual environment created successfully.
    )
)

ECHO Installing packages into virtual environment...
START CMD /k ".\venv\Scripts\activate.bat && pip install -r .\requirements.txt && pre-commit install"

PAUSE
