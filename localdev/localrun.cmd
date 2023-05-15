@echo off
SET SONAR_API_URL=https://sonarcloud.io/api
SET SONAR_ORG_KEY=ENTER SONAR ORG KEY HERE
SET SONAR_PROJECT_KEY=ENTER SONAR PROJECT KEY HERE
SET SONAR_TOKEN=ENTER SONAR TOKEN HERE
SET OPENAI_API_KEY=ENTER OPENAI API KEY HERE
SET GITHUB_OWNER=ENTER
SET GITHUB_REPO_NAME=ENTER REPO NAME HERE
SET GITHUB_ACCESS_TOKEN=ENTER GITHUB ACCESS TOKEN HERE
SET GITHUB_USERNAME=ENTER GITHUB USERNAME HERE
SET GITHUB_EMAIL=ENTER EMAIL HERE
SET MAX_CYCLES=5
SET POLLING_INTERVAL=15

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