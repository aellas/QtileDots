#!/usr/bin/env bash

# Use clipmenu to select an item from clipboard history and set it to clipboard
selection=$(clipmenu | rofi -dmenu -p "Clipboard:" -l 10)

# If a selection was made, copy it to the clipboard using xclip
if [ -n "$selection" ]; then
    echo "$selection" | xclip -selection clipboard
fi