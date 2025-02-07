#!/bin/bash

# Color codes
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m' # Added yellow for headings
BLUE='\e[34m'
RESET='\e[0m'

echo ""

# Get hostname
HOSTNAME=$(hostname)

# Get window manager (WM)
WM=$(wmctrl -m | grep Name | awk '{print $2}')

# Get kernel version
KERNEL=$(uname -r)

# Get system uptime
UPTIME=$(uptime --pretty | sed 's/up //')

# Get number of packages installed (for NixOS - using pacman as requested)
PACKAGE_COUNT=$(pacman -Q | grep -v '^$' | wc -l)

# Get shell
SHELL=$(basename "$SHELL")

# Get CPU info
CPU=$(lscpu | grep 'Model name' | awk -F: '{print $2}' | sed 's/^[[:space:]]*//')

# Get GPU info
GPU=$(lspci | grep -i vga | awk -F: '{print $3}')

# Get RAM usage
RAM=$(free -h | grep Mem | awk '{print $3 "/" $2}')

# Get OS name (for NixOS)
os_name=$(grep -oP '(?<=^PRETTY_NAME=).+' /etc/os-release | tr -d '"')

days=$(sh /home/array/.config/fastfetch/days.sh)

# Display information with color
echo -e " ${BLUE}OS${RESET}----- ${GREEN}$os_name${RESET}"
echo -e " ${BLUE}WM${RESET}----- ${GREEN}$WM${RESET}"
echo -e " ${BLUE}UP${RESET}----- ${GREEN}$UPTIME${RESET}"
echo -e " ${BLUE}KRN${RESET}---- ${GREEN}$KERNEL${RESET}"
echo -e " ${BLUE}PKG${RESET}---- ${GREEN}$PACKAGE_COUNT${RESET}"
echo -e " ${BLUE}DAY${RESET}---- ${GREEN}$days${RESET}"
echo "" # Added an empty line at the end for better formatting
