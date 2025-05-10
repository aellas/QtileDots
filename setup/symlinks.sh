#!/bin/bash

dotfiles_dir="$HOME/Documents/void/QtileDots/.config"
target_dir="/home/array/.config"

echo "Moving dotfiles from $dotfiles_dir to $target_dir..."

# Function to create symlink if it doesn't already exist
create_symlink() {
  local target="$1"
  local link="$2"
  
  if [ -L "$link" ]; then
    echo "Symlink for $link already exists, skipping."
  else
    echo "Linking $target to $link"
    ln -sfn "$target" "$link"
  fi
}

# Symlink for specified directories
for dir in qtile rofi kitty picom dunst fastfetch nvim; do
  target="$dotfiles_dir/$dir"
  link="$target_dir/$dir"
  create_symlink "$target" "$link"
done

echo "Dotfiles setup complete!"
