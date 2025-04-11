#xrandr --output eDP-1 --off
xrandr --output DP-1 --mode 1920x1080 --rate 239.76
/usr/libexec/polkit-gnome-authentication-agent-1 &
dunst -conf ~/.config/dunst/dunstrc &
picom --daemon --config $HOME/.config/qtile/scripts/picom.conf &
xclip &
greenclip daemon &
sudo liquidctl --match corsair initialize --pump-mode balanced > /dev/null 2>&1
sudo liquidctl --match corsair set fan speed 32 20 33 30 34 38 36 50 38 72 40 85 42 100 > /dev/null 2>&1
#xinput set-prop "SynPS/2 Synaptics TouchPad" "Synaptics Tap Action" 1, 0, 3, 0, 0, 0, 0 &
