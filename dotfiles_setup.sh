#!/bin/bash

dotfiles_dir=$(dirname "$(realpath "$0")")

echo "Moving dotfiles..."

cd "$dotfiles_dir" || { echo "Directory not found: $dotfiles_dir"; exit 1; }

# Ensure .themes and .fonts exist
mkdir -p "$HOME/.themes" "$HOME/.fonts"

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

# Symlink contents of themes and fonts directories directly
for theme in "$dotfiles_dir/themes"/*; do
  create_symlink "$theme" "$HOME/.themes/$(basename "$theme")"
done

for font in "$dotfiles_dir/fonts"/*; do
  create_symlink "$font" "$HOME/.fonts/$(basename "$font")"
done

# Symlink for other directories, excluding themes and fonts
for dir in qtile rofi kitty picom dunst fastfetch nvim; do
  target="$dotfiles_dir/$dir"
  link="$HOME/.config/$dir"
  create_symlink "$target" "$link"
done

echo "Dotfiles setup complete!"
