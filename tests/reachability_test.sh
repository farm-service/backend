#!/bin/bash

URL="http://localhost:8000/api/v1/test"
STATUS_CODE=$(curl -o /dev/null -s -w "%{http_code}\n" "$URL")
if [ $? -ne 0 ]; then
  echo "Error: Failed to reach $URL" >> $GITHUB_STEP_SUMMARY
  exit 1
fi
if [[ ! $STATUS_CODE =~ ^2 ]]; then
  echo "Error: Received HTTP status code $STATUS_CODE" >> $GITHUB_STEP_SUMMARY
  exit 1
fi
echo "Success: Received HTTP status code $STATUS_CODE" >> $GITHUB_STEP_SUMMARY