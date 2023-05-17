@echo off
# PROD CONSTANTS
SONAR_API_URL = "https://sonarcloud.io/api"
SONAR_ORG_KEY = os.environ["SONAR_ORGANIZATION_KEY"]
SONAR_PROJECT_KEY = os.environ["SONAR_PROJECT_KEY"]
SONAR_TOKEN = os.environ["SONAR_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
GITHUB_OWNER = os.environ["GITHUB_OWNER_ENV"]
GITHUB_REPO_NAME = os.environ["GITHUB_REPO_NAME_ENV"]
GITHUB_ACCESS_TOKEN = "os.environ['GITHUB_ACCESS_TOKEN_ENV']"
GITHUB_USERNAME = os.environ["GITHUB_USERNAME_ENV"]
GITHUB_EMAIL = os.environ["GITHUB_EMAIL_ENV"]
MAX_CYCLES = int(os.environ.get("MAX_CYCLES", 3))  # Default value is 3 cycles
POLLING_INTERVAL = 15  # Seconds to wait between polling for new issues

REM Move to the root directory of the repository
cd ..

REM Create and activate the virtual environment
python -m venv venv
call venv\Scripts\activate.bat

REM Upgrade pip
python.exe -m pip install --upgrade pip

REM Install dependencies
pip install -r gptscripts\python\requirements.txt

REM Run the Python scripts

REM This script to confirm that folders structure is up to date
python gptscripts\python\debugfiles\cmdscripttest.py

REM This script will exxecute one run of the fixer without a continuous improvement loop
REM python gptscripts\python\debugfiles\single_run_fix.py

REM This script will exxecute the fixer with a continuous improvement loop
REM python gptscripts\python\debugfiles\sf_bunch.py

REM Deactivate the virtual environment
call venv\Scripts\deactivate.bat