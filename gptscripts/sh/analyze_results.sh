#!/bin/bash

set -e

# Set your variables
SONAR_API_URL="https://sonarcloud.io/api"
SONAR_ORG_KEY="odegay"
SONAR_PROJECT_KEY=""
SONAR_TOKEN=""

# Retrieve the list of issues
response=$(curl -s -w "%{http_code}" -G \
  -H "Authorization: Basic $(echo -n "${SONAR_TOKEN}" )" \
  --data-urlencode "organization=${SONAR_ORG_KEY}" \
  --data-urlencode "projects=${SONAR_PROJECT_KEY}" \
  --data-urlencode "ps=500" \
  --data-urlencode "types=BUG, VULNERABILITY, CODE_SMELL" \
  --data-urlencode "statuses=OPEN, CONFIRMED" \
  "${SONAR_API_URL}/issues/search")

# Extract the response code and body
response_code=$(echo "$response" | tail -n1)
response_body=$(echo "$response" | head -n-1)

if [ "$response_code" -ne 200 ]; then
  echo "Error: Unable to fetch issues from SonarCloud API (HTTP $response_code)" >&2
  exit 1
fi

# Extract the suggested fixes using jq and output them as a JSON array
fixes=$(echo "$response_body" | jq -r '[.issues[] | .message]')

echo "$fixes"
echo $issues
echo $fixes
echo "work is done"
