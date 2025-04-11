#!/bin/bash

# Define themes with their corresponding config identifiers
declare -A themes
themes=(
    ["Custom"]="theme1"
    ["Catppuccin-Mocha"]="theme2"
    ["E-Ink Light"]="theme3"
    ["Gruvbox"]="theme4"
    ["Ocean"]="theme5"
    ["E-Ink Dark"]="theme6"
)

# Path to Qtile config
QTILE_CONFIG="$HOME/.config/qtile/config.py"
STATE_FILE="$HOME/.config/qtile/current_theme"

# Read last theme (if exists)
if [ -f "$STATE_FILE" ]; then
    last_theme=$(cat "$STATE_FILE")
else
    last_theme="Custom"
fi

# Show Rofi menu
chosen_theme=$(printf "%s\n" "${!themes[@]}" | rofi -dmenu -p "Select Theme:")

# If no selection, exit
[ -z "$chosen_theme" ] && exit 1

# Get the corresponding theme variable name
theme_var="${themes[$chosen_theme]}"

# Update the Qtile config to set the new theme
sed -i "s/^current_theme = .*/current_theme = $theme_var/" "$QTILE_CONFIG"

# Save selected theme for persistence
echo "$chosen_theme" > "$STATE_FILE"

# Restart Qtile to apply changes
qtile cmd-obj -o cmd -f reload_config
