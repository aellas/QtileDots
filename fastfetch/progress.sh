#!/bin/bash

# Define the start date
start_date="2025-04-09"

# Calculate the end date (2 years later)
end_date=$(date -d "$start_date + 2 years" +%Y-%m-%d)

# Get today's date
today=$(date +%Y-%m-%d)

# Calculate total duration and days passed
total_days=$(( ( $(date -d "$end_date" +%s) - $(date -d "$start_date" +%s) ) / 86400 ))
days_passed=$(( ( $(date -d "$today" +%s) - $(date -d "$start_date" +%s) ) / 86400 ))

# Cap progress at 100%
if [ "$days_passed" -gt "$total_days" ]; then
    days_passed=$total_days
fi

# Calculate progress percentage
progress_percent=$(awk "BEGIN { printf \"%.2f\", ($days_passed / $total_days) * 100 }")

# Print progress
echo "$progress_percent%"
