import os

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from functions import smart_swap

mod = "mod4"
terminal = "kitty"
webBrowser = "brave"
fileExplorer = "nemo"
appLauncher = "rofi -show drun"
screenshotFull = "flameshot full --clipboard --path /home/array/Pictures/Screenshots"
prismLauncher = "prismlauncher"
youtubeMusic = "youtube-music"
boltLauncher = "bolt"
vesktop = "vesktop"
gpick = "gpick --pick"
gemini = "brave --app=https://gemini.google.com/app"
steam = "steam"
github = "github-desktop"
code = "neovide"

keys = [

    # My Keybinds
    Key([mod], "return", lazy.spawn(terminal), desc="Launch terminal"), # kitty
    Key([mod], "b", lazy.spawn(webBrowser), desc="Launch web browser"), # brave browser
    Key([mod], "n", lazy.spawn(fileExplorer), desc="Launch file explorer"), # nemo
    Key([mod], "SPACE", lazy.spawn(appLauncher), desc="Launch rofi"), # rofi
    Key([mod], "j", lazy.spawn(boltLauncher), desc="Launch bolt launcher"), #bolt launcher
    Key([mod], "m", lazy.spawn(youtubeMusic), desc="Launch youtube music"), # youtube music
    Key([mod], "backslash", lazy.spawn(code), desc="Launch vscode"), # vscode
    Key([mod], "d", lazy.spawn(vesktop), desc="Launch vesktop"), # vesktop
    Key([mod], "p", lazy.spawn(prismLauncher), desc="Launch prism launcher"), # prism launcher 
    Key([mod], "c", lazy.spawn(gpick), desc="Launch gpick"), # gpick
    Key([mod], "s", lazy.spawn(steam), desc="Launch steam"), # steam
    Key([mod], "p", lazy.spawn(github), desc="Launch Github"), # gemini
    Key([mod], "g", lazy.spawn(gemini), desc="Launch gemini"), # gemini
    Key([], "Home", lazy.spawn(screenshotFull), desc="Take a screenshot"), # flameshot


    Key([mod], "Left", lazy.layout.shrink()),
    Key([mod], "Right", lazy.layout.grow()),
    Key([mod], "r", lazy.layout.reset(), desc="Reset layout to default"), # Reset the current layout

    # Custom Binds
    Key([mod], "tab", lazy.function(smart_swap), desc="Smart Swap"), # Custom swap 
    #Key([mod], "tab", lazy.layout.swap_main()), # Swap with main
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"), # toggle fullscreen
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"), # toggle floating
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Logout"), # logout
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"), # reload qtile
    Key([mod], "q", lazy.window.kill()), # kill focused window
    Key([mod, "shift"], "m", lazy.window.toggle_maximize(), desc="Toggle maximize"),

    # Audio Binds
    Key([], "XF86AudioRaiseVolume", lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ +2%'), desc="Up the volume"), # volume up 
    Key([], "XF86AudioLowerVolume", lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ -2%'), desc="Down the volume"), # volume down
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


group_labels = {
        "1": "",
        "2": "",
        "3": "󰝚",
        "4": "󰵅",
        "5": "󰊖",
        "6": "󰄀"
}


groups = [Group(name, label=label) for name, label in group_labels.items()]
for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name),),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False), desc="Move focused window to group {}".format(i.name),),
        ]
    )

layouts = [
    layout.MonadTall(border_width=2, border_focus="#C9C0C9", border_normal="#494E5E", margin=6, fair=True),
]


groups.append(ScratchPad("scratchpad", [
    DropDown("term", "kitty --class=scratch", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.95),
    DropDown("volume", "pavucontrol", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("htop", "kitty --class=scratch -e htop", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("protonmail", "brave-browser-stable --app=https://mail.proton.me/u/0/inbox", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("protondrive", "brave-browser-stable --app=https://drive.proton.me/u/0/", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),


]))

# Scratchpad keybindings
keys.extend([
    Key([mod], "v", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], "o", lazy.group['scratchpad'].dropdown_toggle('volume')),
    Key([mod], "h", lazy.group['scratchpad'].dropdown_toggle('htop')),


])

def longNameParse(text):
    for string in ["Brave", "Code"]:  # Order from longest to shortest
        if string.lower() in text.lower():  # Case-insensitive comparison
            return string  # Return immediately after finding a match
    return text  # Return original text if no match is found

widget_defaults = dict(
    font="Ubuntu Nerd Font Bold",
    fontsize=14,
    padding=3,
    foreground="#ffffff",
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [    
                widget.Spacer(
                    length=10,
                    background="#0B0C0F"
                ),
                widget.TextBox(
                    fmt="  ", 
                    background="#0B0C0F", 
                    foreground="#00a489", 
                ),
                widget.Spacer(
                    length=5, 
                    background="#0B0C0F"
                ),
                widget.GroupBox(
                    font="Ubuntu Nerd Font",
                    font_size="14",
                    margin_y=3,
                    margin_x=2,
                    padding_y=5.5,
                    padding_x=5,
                    background="#0B0C0F",
                    active="#ffffff",
                    inactive="#ffffff",
                    rounded=True,
                    highlight_method="block",
                    block_highlight_text_color="#0b0c0f",
                    this_screen_border="#D3C9D2",
                    this_current_screen_border="#D3C9D2",
                    urgent_border="#D3C9D2",
                    urgent_text="#0b0c0f"
                ),
                widget.Spacer(
                    length=15, 
                    background="#0B0C0F"
                ),
                widget.WindowName(
                    format = "  {name}", 
                    parse_text=longNameParse,
                    background="#0B0C0F", 
                    foreground="#ffffff",  
                ),
                widget.Mpris2(
                    fmt="   {}", 
                    format="{xesam:artist} - {xesam:title}", 
                    background="#0B0C0F", 
                    foreground="#ffffff", 
                    max_chars=150, 
                ),
                widget.Spacer(
                    length=15,
                    background="#0B0C0F",
                ),
                widget.Systray(
                    background="#0B0C0F",
                    icon_size=17,
                ),
                widget.Spacer(
                    length=15,
                    background="#0B0C0F",
                ),
                widget.Volume(
                    fmt="  {}",
                    background="#0B0C0F",
                    foreground="#ffffff",
                ),
                widget.Spacer(
                    length=15,
                    background="#0B0C0F",
                ),
                widget.TextBox(
                    fmt="  ", 
                    background="#0B0C0F", 
                    foreground="#ffffff", 
                ),
                widget.Spacer(
                    length=15, 
                    background="#0B0C0F"
                ),
                widget.Clock(
                    format="%H:%M", 
                    foreground="#ffffff", 
                    background="#0B0C0F", 
                ),
                widget.Spacer(
                    length=15, 
                    background="#0B0C0F"
                ),
                widget.QuickExit(
                    fmt="", 
                    background="#0B0C0F", 
                    foreground="#F95353"
                ),
                widget.Spacer(
                    length=15, 
                    background="#0B0C0F"
                ),
            ],
            40,
            background = "#0B0C0F",
            opacity = 1.0,
            margin = [6,6,0,6]
        ),
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = True
floating_layout = layout.Floating(
    border_width=2,
    border_focus="#C8C0C9",
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),
 # gitk
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
os.system("bash ~/.config/qtile/autostart.sh")
wmname = "qtile"
