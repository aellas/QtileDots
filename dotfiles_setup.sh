#!/bin/bash

dotfiles_dir=$(dirname "$(realpath "$0")")

echo "Moving dotfiles..."

cd "$dotfiles_dir" || { echo "Directory not found: $dotfiles_dir"; exit 1; }

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

# Symlink for other directories, excluding themes and fonts
for dir in qtile rofi kitty picom dunst fastfetch nvim; do
  target="$dotfiles_dir/$dir"
  link="$HOME/.config/$dir"
  create_symlink "$target" "$link"
done

echo "Dotfiles setup complete!"
