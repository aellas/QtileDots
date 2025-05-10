#!/usr/bin/env bash

# Directory containing wallpapers
WALLPAPER_DIR="$HOME/Documents/void/QtileDots/wallpapers/"

# Use rofi to select a wallpaper
SELECTED=$(find "$WALLPAPER_DIR" -type f | sort | rofi -dmenu -i -p "Select Wallpaper")

# Exit if no selection made
[ -z "$SELECTED" ] && exit 1

# Set wallpaper using feh
feh --bg-fill "$SELECTED"

# Generate pywal colors
wal -i "$SELECTED"

# Reload Qtile config
qtile cmd-obj -o cmd -f reload_config

bash dunst.sh
