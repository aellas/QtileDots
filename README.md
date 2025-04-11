<p align="center">QtileDots</p>
<div align="center">
  <img src="https://img.shields.io/github/stars/aellas/QtileDots?style=for-the-badge&logo=starship&color=83c5be&logoColor=D9E0EE&labelColor=252733" alt="Stars">
  <img src="https://img.shields.io/github/last-commit/aellas/QtileDots?style=for-the-badge&color=006d77&logoColor=D9E0EE&labelColor=252733" alt="Last Commit">
  <a href="https://github.com/aellas/QtileDots/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/aellas/QtileDots?style=for-the-badge&logo=starship&color=1d3557&logoColor=D9E0EE&labelColor=252733" />
  </a>
</div>

<p align="center">This repository contains my configuration files for the Qtile window manager</p>

## Optional
Both scripts are designed to get my dotfiles fully working for myself on Void and the software I use, please use at your own risk! I've included them incase someone was interested :)
1. **`setup_void.sh`**: This script is designed to help setup your Void install for Qtile
2. **`dotfiles_setup.sh`**: This script installs and links your dotfiles into the correct locations for easy management..

![preview](preview/preview1.png?raw=true)

## Software

- Distro: [Void](https://voidlinux.org/)
- WM: [Qtile](https://qtile.org/)
- Compositor: [Picom](https://github.com/yshui/picom)
- Bar: [Qtile Bar](https://qtile.org/)
- Shell: [Fish](https://fishshell.com/)
- Font: [Ubuntu Nerd Font](https://www.nerdfonts.com/font-downloads)
- GTK-Theme: [MonoThemeDark (edited)](https://github.com/witalihirsch/Mono-gtk-theme))
- Terminal: [Kitty](https://sw.kovidgoyal.net/kitty/)
- Launcher: [Rofi](https://github.com/davatorium/rofi)
- File Manager: [Yazi](https://github.com/sxyazi/yazi)
- Screenshots: [flameshot](https://flameshot.org/)
- Notification: [Dunst](https://github.com/dunst-project/dunst)
- Image Viewer: [Feh](https://feh.finalrewind.org/)
- Media Player: [mpv](https://github.com/mpv-player/mpv)

## Theme Selector

This setup includes a **basic theme selector** that allows you to quickly change between different themes, please see **Keybinds** on how to switch themes.


## Main Keybinds

| Keybind | Description |
|---|---|
| Mod + Enter | Launch Terminal |
| Mod + Space | Launch Rofi |
| Mod + B | Open Web Browser |
| Mod + N | Open Filemanager |
| Mod + X | Gpick Color Picker |
| Mod + M | Open Youtube Music |
| Home | Take Full Screen Screenshot |
| Mod + Home | Take Region Screenshot |
| Mod + Q | Kill window |
| Mod + K | Greenclip + Rofi Clipboard Manager |
| Mod + SHIFT + Q | Exit Qtile |
| Mod + SHIFT + R | Reload Qtile |
| Mod + SHIFT + T | Switch Themes |

## Credits
- [Bitterhalt](https://github.com/bitterhalt) - For tons of inspiration 🐐
- [TheLinuxCast](https://gitlab.com/thelinuxcast) - For coverage on Qtile + Supplying the symlinks bash script <3
- [CachyOS](https://cachyos.org/) - For the preconfigured Qtile dots that helped me start my journey with Qtile
