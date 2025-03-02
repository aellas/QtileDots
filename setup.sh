dotfiles = "/home/$USER/Documents/QtileDots"

echo "moving dotfiles"

cd $dotfiles
ln -s /home/$USER/Documents/QtileDots/qtile ~/.config
ln -s /home/$USER/Documents/QtileDots/rofi ~/.config
ln -s /home/$USER/Documents/QtileDots/kitty ~/.config
ln -s /home/$USER/Documents/QtileDots/picom ~/.config
ln -s /home/$USER/Documents/QtileDots/dunst ~/.config
ln -s /home/$USER/Documents/QtileDots/fastfetch ~/.config
ln -s /home/$USER/Documents/QtileDots/nvim ~/.config
