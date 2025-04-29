from libqtile import hook
import subprocess
import os

theme3 = { #custom
    "background": "#0F1014",
    "foreground": "#e1e6ff",
    "background2": "#8EB6F5",
    "background3": "#8A8BB1",
    "active": "#ffffff",
    "inactive": "#ffffff",
    "border_focus": "#C9C0C9",
    "border_normal": "#14161B",
    "block_highlight_text_color": "#0F1014",
    "this_screen_border": "#D3C9D2",
    "this_current_screen_border": "#D3C9D2",
    "urgent_border": "#D3C9D2",
    "urgent_text": "#0F1014",
    "wallpaper": "~/.config/qtile/themes/wallpapers/what.jpg",
    "gtk_theme": "Space-dark",
    "kitty_theme": "default.conf",
}

theme2 = { # eink-light
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
    "kitty_theme": "eink.conf",
}

theme1 = {
"background": "#0A0A0A",
    "foreground": "#D2D2D2",
    "background2": "#D8D8D8",
    "active": "#D8D8D8",
    "inactive": "#D8D8D8",
    "border_focus": "#e1e6ff",
    "border_normal": "#e1e6ff",
    "block_highlight_text_color": "#171922",
    "this_screen_border": "#e1e6ff",
    "this_current_screen_border": "#D8D8D8",
    "urgent_border": "#ff5555",
    "urgent_text": "#282828",
    "wallpaper": "~/.config/qtile/themes/wallpapers/roses.jpg",
    "gtk_theme": "MonoThemeDark",
    "kitty_theme": "monochrome.conf",
}

theme4 = {
    "background": "#0A0A0A",
    "foreground": "#DBDBDB",
    "background2": "#F8F9FA",
    "active": "#D8D8D8",
    "inactive": "#D8D8D8",
    "border_focus": "#B5B5B5",
    "border_normal": "#B5B5B5",
    "block_highlight_text_color": "#171922",
    "this_screen_border": "#B5B5B5",
    "this_current_screen_border": "#B5B5B5",
    "urgent_border": "#ff5555",
    "urgent_text": "#282828",
    "wallpaper": "~/.config/qtile/themes/wallpapers/monochrome/waters.jpg",
    "gtk_theme": "MonoThemeDark",
    "kitty_theme": "monochrome.conf",
}




if 'current_theme' not in globals():
    current_theme = theme1

def switch_theme(qtile):
    global current_theme
    if current_theme == theme1:
        current_theme = theme2
    elif current_theme == theme2:
        current_theme = theme3
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
