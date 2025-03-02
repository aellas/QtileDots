#!/bin/bash

# Define colors for aesthetics
bold="\e[1m"
reset="\e[0m"

# Logo (replace with your actual path)
logo_path="$HOME/.config/fastfetch/fastfetch.png"

# Get system information
username=$(whoami)
hostname=$(hostname)
distro=$(grep -E '^PRETTY_NAME=' /etc/os-release | cut -d= -f2 | tr -d '"')
kernel=$(uname -r)
packages=$(xbps-query -l | wc -l)
terminal="$TERM"
uptime=$(uptime -p | sed 's/up //')
day=$(bash ~/.config/fastfetch/days.sh)

# WM Detection (Qtile on X11)
wm=$(xprop -root _NET_SUPPORTING_WM_CHECK | awk '{print $5}' | xargs xprop -id | grep "_NET_WM_NAME" | cut -d '"' -f2)
[ -z "$wm" ] && wm="Qtile" # Fallback in case detection fails

# Display image on the left
if [ -f "$logo_path" ] && command -v kitty >/dev/null; then
  kitty +kitten icat --align=left --scale-up "$logo_path"
fi

# Add a slight delay to let the image render before printing text
sleep 0.1

# Display system info in a beautiful box
printf "${bold}+-------------------------------+${reset}\n"
printf "${bold}|           %s@%s${reset}\n" "$username" "$hostname           |"
printf "${bold}+-------------------------------+${reset}\n"
printf "${bold}|   Distro      :${reset} %s\n"     "$distro   |"
printf "${bold}|   Kernel      :${reset} %s\n" "$kernel"
printf "${bold}|       WM      :${reset} %s\n" "$wm"
printf "${bold}| Packages :${reset} %s\n" "$packages"
printf "${bold}| Terminal :${reset} %s\n" "$terminal"
printf "${bold}|   Uptime   :${reset} %s\n" "$uptime"
printf "${bold}|      Day      :${reset} %s\n" "$day"
printf "${bold}+-------------------------------+${reset}\n"

echo "" # Final newline
