#!/usr/bin/env bash

# Set the base directory to search for git repos (change as needed)
BASE_DIR="$HOME"

# Find all git repositories
REPOS=$(find "$BASE_DIR" -type d -name ".git" -prune | sed 's|/.git||')

# Use fzf to select one repo
SELECTED_REPO=$(echo "$REPOS" | fzf --prompt="Select Git Repo > ")

# Exit if nothing selected
[ -z "$SELECTED_REPO" ] && echo "No repo selected." && exit 1

# Navigate to the selected repo
cd "$SELECTED_REPO" || exit 1

# Show repo name
echo "Working on $(basename "$SELECTED_REPO")"

# Stage changes
git add .

# Ask for commit message
read -rp "Enter commit message: " COMMIT_MSG

# Commit
git commit -m "$COMMIT_MSG"

# Pull latest changes
git pull --rebase

# Push to remote
git push

echo "✅ Done with $(basename "$SELECTED_REPO")"
