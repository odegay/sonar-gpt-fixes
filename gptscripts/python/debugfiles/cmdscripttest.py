import os
import requests
import openai
import base64
import sys
import tempfile
import time
import copy
from git import Repo
from datetime import datetime

# Set up environment variables
SONAR_API_URL = "https://sonarcloud.io/api"
SONAR_ORG_KEY = os.environ["SONAR_ORG_KEY"]
SONAR_PROJECT_KEY = os.environ["SONAR_PROJECT_KEY"]
SONAR_TOKEN = os.environ["SONAR_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
GITHUB_OWNER = os.environ["GITHUB_OWNER"]
GITHUB_REPO_NAME = os.environ["GITHUB_REPO_NAME"]
GITHUB_ACCESS_TOKEN = os.environ["GITHUB_ACCESS_TOKEN"]
GITHUB_USERNAME = os.environ["GITHUB_USERNAME"]
GITHUB_EMAIL = os.environ["GITHUB_EMAIL"]
MAX_CYCLES = int(os.environ.get("MAX_CYCLES", 3))  # Default value is 3 cycles
POLLING_INTERVAL = 15  # Seconds to wait between polling for new issues

def main():
    print("script started")

    print("Environment variables:")
    print("SONAR_API_URL: " + SONAR_API_URL)
    print("SONAR_ORGANIZATION_KEY: " + SONAR_ORG_KEY)
    print("SONAR_PROJECT_KEY: " + SONAR_PROJECT_KEY)
    print("SONAR_TOKEN: " + SONAR_TOKEN)
    print("OPENAI_API_KEY: " + OPENAI_API_KEY)
    print("GITHUB_OWNER: " + GITHUB_OWNER)
    print("GITHUB_REPO_NAME: " + GITHUB_REPO_NAME)
    print("GITHUB_ACCESS_TOKEN: " + GITHUB_ACCESS_TOKEN)
    print("GITHUB_USERNAME: " + GITHUB_USERNAME)
    print("GITHUB_EMAIL: " + GITHUB_EMAIL)
    print("MAX_CYCLES: " + str(MAX_CYCLES))
    print("POLLING_INTERVAL: " + str(POLLING_INTERVAL))

    print("script finished")

if __name__ == "__main__":
    main()