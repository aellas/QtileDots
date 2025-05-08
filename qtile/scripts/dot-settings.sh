#!/usr/bin/env bash

# Base terminal command
TERMCMD=("kitty")

# First menu options
OPTIONS="QTILEDIR
QTILECONFIG
KITTY
ROFI
PICOM
NEOVIM
DUNST"

CHOICE=$(printf "$OPTIONS" | rofi -dmenu -p "Edit settings:")

if [[ "$CHOICE" == "QTILEDIR" ]]; then
    QTILE_DIR="$HOME/Documents/void/QtileDots/qtile"
    QTILE_FILES=$(find -L "$QTILE_DIR" -type f)
    if [[ -z "$QTILE_FILES" ]]; then
        notify-send "No files found in $QTILE_DIR"
        exit 1
    fi
    QTILE_FILE=$(printf "%s\n" "$QTILE_FILES" | sed "s|$HOME/||" | rofi -dmenu -p "Select Qtile file")
    [[ -n "$QTILE_FILE" ]] && "${TERMCMD[@]}" -e nvim "$HOME/$QTILE_FILE"
    exit
fi
# Main choices
case $CHOICE in
    QTILECONFIG) "${TERMCMD[@]}" -e nvim "$HOME/Documents/void/QtileDots/qtile/config.py" ;;
    KITTY) "${TERMCMD[@]}" -e nvim "$HOMEDocuments/void/QtileDots/kitty/kitty.conf" ;;
    ROFI) "${TERMCMD[@]}" -e nvim "$HOME/Documents/void/QtileDots/rofi/config.rasi" ;;
    PICOM) "${TERMCMD[@]}" -e nvim "$HOME/Documents/void/QtileDots/picom/picom.conf" ;;
    NEOVIM) "${TERMCMD[@]}" -e nvim "$HOME/.config/Documents/void/QtileDots/nvim/init.lua" ;;
    DUNST) "${TERMCMD[@]}" -e nvim "$HOME/Documents/void/QtileDots/dunst/dunst.rc" ;;
esac