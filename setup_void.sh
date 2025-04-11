#!/bin/bash

# Update package repositories
echo "Updating package repositories..."
sudo xbps-install -Su

# Install packages
echo "Installing packages..."
sudo xbps-install -y \
  qtile \
  python3-qtile-extras \
  picom \
  qtile \
  feh \
  kitty \
  flameshot \
  mpv \
  dunst \
  yazi \
  noto-fonts-cjk \
  noto-fonts-emoji \
  void-repo-nonfree \
  void-repo-multilib \
  void-repo-multilib-nonfree \
  pulseaudio \
  pulseaudio-utils \
  pulsemixer \
  alsa-plugins-pulseaudio \
  bluez \
  cronie \
  dbus \
  elogind \
  git \
  ufw \
  nwg-look \
  neovim \
  pyright \


# Enable services
echo "Enabling services..."
sudo ln -s /etc/sv/bluetoothd /var/service
sudo ln -s /etc/sv/cronie /var/service
sudo ln -s /etc/sv/dbus /var/service
sudo ln -s /etc/sv/elogind /var/service
sudo ln -s /etc/sv/ufw /var/service/ufw

echo "Adding Bluetooth to usergroup..."
sudo useradd -G bluetooth ${USER}

echo "Enabling UFW (firewall)"
sudo ufw enable

echo "Downloading and installing greenclip..."
wget https://github.com/erebe/greenclip/releases/download/v4.2/greenclip -O /usr/local/bin/greenclip
sudo chmod +x /usr/local/bin/greenclip

echo "Setup completed!"
