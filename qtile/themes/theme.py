from libqtile import hook
import subprocess
import os

theme1 = { #custom
    "background": "#0F1014",
    "foreground": "#ffffff",
    "background2": "#009E85",
    "active": "#ffffff",
    "inactive": "#ffffff",
    "border_focus": "#C9C0C9",
    "border_normal": "#14161B",
    "block_highlight_text_color": "#0F1014",
    "this_screen_border": "#D3C9D2",
    "this_current_screen_border": "#D3C9D2",
    "urgent_border": "#D3C9D2",
    "urgent_text": "#0F1014",
    "wallpaper": "~/.config/qtile/themes/wallpapers/orange.jpg",
    "gtk_theme": "Space-dark",
    "kitty_theme": "default.conf",
}

theme2 = { #catpuccin-mocha
    "background": "#11111B",
    "foreground": "#f8f8f2",
    "background2": "#A6DA95",
    "active": "#f8f8f2",
    "inactive": "#f8f8f2",
    "border_focus": "#CAD3F5",
    "border_normal": "#CAD3F5",
    "block_highlight_text_color": "#11111B",
    "this_screen_border": "#CAD3F5",
    "this_current_screen_border": "#CAD3F5",
    "urgent_border": "#ff5555",
    "urgent_text": "#282828",
    "wallpaper": "~/.config/qtile/themes/wallpapers/koi.jpg",
    "kitty_theme": "mocha.conf",
}

theme3 = { # eink
    "background": "#BEBEBE",
    "foreground": "#3A3A3A",
    "background2": "#3A3A3A",
    "active": "#3A3A3A",
    "inactive": "#3A3A3A",
    "border_focus": "#C9C0C9",
    "border_normal": "#14161B",
    "block_highlight_text_color": "#BEBEBE",
    "this_screen_border": "#3A3A3A",
    "this_current_screen_border": "#3A3A3A",
    "urgent_border": "#FEFEFE",
    "urgent_text": "#3A3A3A",
    "wallpaper": "~/.config/qtile/themes/wallpapers/as.png",
    "gtk_theme": "Graphite-Light",
    "kitty_theme": "eink.conf",
}

theme4 = { # Gruvbox
    "background": "#282828",
    "foreground": "#D4BE97",
    "background2": "#689D6A",
    "active": "#D4BE97",
    "inactive": "#D4BE97",
    "border_focus": "#98971A",
    "border_normal": "#98971A",
    "block_highlight_text_color": "#282828",
    "this_screen_border": "#98971A",
    "this_current_screen_border": "#98971A",
    "urgent_border": "#ff5555",
    "urgent_text": "#282828",
    "wallpaper": "~/.config/qtile/themes/wallpapers/4.png",
    "kitty_theme": "gruvbox.conf",
}
theme5 = {
    "background": "#1B1E28",
    "foreground": "#C8CFDA",
    "background2": "#5DE4C7",
    "active": "#C8CFDA",
    "inactive": "#C8CFDA",
    "border_focus": "#A6ACCD",
    "border_normal": "#A6ACCD",
    "block_highlight_text_color": "#171922",
    "this_screen_border": "#A6ACCD",
    "this_current_screen_border": "#A6ACCD",
    "urgent_border": "#ff5555",
    "urgent_text": "#282828",
    "wallpaper": "~/.config/qtile/themes/wallpapers/ocean.jpg",
    "kitty_theme": "pomi.conf",
}
if 'current_theme' not in globals():
    current_theme = theme1

def switch_theme(qtile):
    global current_theme
    if current_theme == theme1:
        current_theme = theme2
    elif current_theme == theme2:
        current_theme = theme3
    elif current_theme == theme3:
        current_theme = theme4
    elif current_theme == theme4:
        current_theme = theme5
    else:
        current_theme = theme1
    wallpaper_path = os.path.expanduser(current_theme["wallpaper"])
    subprocess.run(["feh", "--bg-fill", wallpaper_path])
    if "gtk_theme" in current_theme:
        subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", current_theme["gtk_theme"]])

    qtile.reload_config()


@hook.subscribe.startup_once
def set_wallpaper():
    wallpaper_path = os.path.expanduser(current_theme["wallpaper"])

    subprocess.run(["feh", "--bg-fill", wallpaper_path])
