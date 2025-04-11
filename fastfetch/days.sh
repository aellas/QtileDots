#!/bin/bash

# Define the start date
start_date="2025-04-09"

# Get current date
today=$(date +%Y-%m-%d)

# Calculate the number of days since start date
days_since_start=$(($(date -d "$today" +%s) - $(date -d "$start_date" +%s)))
days_since_start=$((days_since_start / 86400))

# Calculate the number of days for 2 years
end_date=$(date -d "$start_date + 2 years" +%Y-%m-%d)
days_for_2_years=$(($(date -d "$end_date" +%s) - $(date -d "$start_date" +%s)))
days_for_2_years=$((days_for_2_years / 86400))

# Print the results
echo "$days_since_start"
