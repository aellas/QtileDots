#!/usr/bin/env bash

# Options for the menu
options="Logout\nReboot\nShutdown\nLock"

# Rofi command for the menu
choice=$(echo -e "$options" | rofi -dmenu -p "Power Menu")

# Actions based on selection
case "$choice" in
  "Logout")
    # Replace with your window manager's logout command
    pkill -u $USER
    ;;
  "Reboot")
    sudo reboot
    ;;
  "Shutdown")
    sudo poweroff -n
    ;;
  "Lock")
    # Lock the screen (adjust command if you use a different locker)
    betterlockscreen -l blur
    ;;
  *)
    exit 1
    ;;
esac
