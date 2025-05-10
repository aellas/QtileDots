import json, os

try:
    with open(os.path.expanduser("~/.cache/wal/colors.json")) as f:
        wal_colors = json.load(f)
except FileNotFoundError:
    print("Warning: ~/.cache/wal/colors.json not found. Using default theme.")
    wal_colors = {
        "special": {"background": "#282a36", "foreground": "#f8f8f2"},
        "colors": {
            "color0": "#282a36", "color1": "#ff5555", "color2": "#50fa7b", "color3": "#f1fa8c",
            "color4": "#bd93f9", "color5": "#ff79c6", "color6": "#8be9fd", "color7": "#f8f8f2",
            "color8": "#6272a4", "color9": "#ff6e6e", "color10": "#69ff94", "color11": "#ffffa5",
            "color12": "#d6acff", "color13": "#ff92df", "color14": "#a4ffff", "color15": "#ffffff",
        }
    }

current_theme = {
    "background": wal_colors["special"]["background"],
    "foreground": wal_colors["special"]["foreground"],
    "active": wal_colors["colors"]["color2"],
    "inactive": wal_colors["colors"]["color8"],
    "block_highlight_text_color": wal_colors["colors"]["color1"],
    "this_screen_border": wal_colors["colors"]["color4"],
    "this_current_screen_border": wal_colors["colors"]["color5"],
    "urgent_border": wal_colors["colors"]["color1"],
    "urgent_text": wal_colors["colors"]["color1"],
    "background2": wal_colors["colors"]["color0"]
}