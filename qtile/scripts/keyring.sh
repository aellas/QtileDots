#!/usr/bin/env bash

# Start gnome-keyring daemons
eval $(/run/current-system/sw/bin/gnome-keyring-daemon --start --components=secrets,pkcs11,ssh)
export SSH_AUTH_SOCK

# Optional: export environment for the current session
echo "SSH_AUTH_SOCK=$SSH_AUTH_SOCK" > ~/.gnome-keyring-env

# Verify it’s running
gnome-keyring-daemon --start --components=secrets,pkcs11,ssh
