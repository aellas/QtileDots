#!/bin/bash

# Define the start date
start_date="2025-04-09"

# Calculate the end date (2 years later)
end_date=$(date -d "$start_date + 2 years" +%Y-%m-%d)

# Get today's date
today=$(date +%Y-%m-%d)

# Calculate remaining days
seconds_left=$(( $(date -d "$end_date" +%s) - $(date -d "$today" +%s) ))
days_left=$((seconds_left / 86400))

# Print remaining days
echo "$days_left"
