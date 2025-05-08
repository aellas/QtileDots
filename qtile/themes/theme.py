import subprocess
import os
import sys
from libqtile import hook

# Path to pywal's generated Python colors
wal_colors_file = os.path.expanduser("~/.cache/wal/colors.py")

# Load pywal colors
colors = None
if os.path.exists(wal_colors_file):
    with open(wal_colors_file) as f:
        code = compile(f.read(), wal_colors_file, 'exec')
        exec(code)  # defines 'colors' list and individual color variables
else:
    # fallback in case pywal hasn't been run yet
    colors = ["#1e1e2e"] * 16

current_theme = {
    "background": colors[0],
    "foreground": colors[7],
    "background2": colors[1],
    "active": colors[6],
    "inactive": colors[4],
    "border_focus": colors[5],
    "border_normal": colors[0],
    "block_highlight_text_color": colors[1],
    "this_screen_border": colors[6],
    "this_current_screen_border": colors[7],
    "urgent_border": colors[1],
    "urgent_text": colors[0],
    "wallpaper": os.path.expanduser("~/.cache/wal/wal"),  # optional
    "gtk_theme": "Adwaita-dark",  # optional, or set by wal-gtk
    "kitty_theme": "pywal.conf",  # optional, if you generate one
}

def run_pywal(image_path):
    subprocess.run(["wal", "-i", image_path, "--quiet"])
    subprocess.run(["feh", "--bg-fill", image_path])
    subprocess.run(["wal-gtk", "-i"])