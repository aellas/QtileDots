#!/bin/bash

choice=$(echo -e "Poweroff\nLogout\nRestart" | rofi -dmenu -p "Action:")

case "$choice" in
    "Poweroff")
        sudo poweroff
        ;;
    "Logout")
        logout
        ;;
    "Restart")
        sudo reboot
        ;;
esac