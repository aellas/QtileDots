#!/usr/bin/env bash
updates=$(xbps-install -Su -n)
if [[ "$updates" != "" ]]; then
  notify-send "Updates Available" "You have updates pending."
else
  notify-send "No Updates" "Your system is up to date."
fi

