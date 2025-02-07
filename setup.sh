dotfiles = "$HOME/dotfiles"

echo "moving dotfiles"

cd $dotfiles
ln -s $HOME/dotfiles/qtile ~/.config
ln -s $HOME/dotfiles/rofi ~/.config
ln -s $HOME/dotfiles/kitty ~/.config
ln -s $HOME/dotfiles/picom ~/.config
ln -s $HOME/dotfiles/dunst ~/.config
ln -s $HOME/dotfiles/fastfetch ~/.config
ln -s $HOME/dotfiles/myfetch ~/.config
ln -s $HOME/dotfiles/nvim ~/.config
