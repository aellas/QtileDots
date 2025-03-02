import os
import subprocess

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras import widget
from libqtile.widget import backlight
from themes.theme import current_theme, switch_theme 
from libqtile import hook
from libqtile.config import Match


from functions import smart_swap

mod = "mod4"
terminal = f"kitty --config /home/array/.config/kitty/{current_theme['kitty_theme']}"
webBrowser = "brave-browser-stable"
fileExplorer = "nemo"
appLauncher = "rofi -show drun"
screenshotFull = "flameshot full --clipboard --path /home/array/Pictures/Screenshots"
prismLauncher = "prismlauncher"
youtubeMusic = '"/opt/YouTube Music/youtube-music" %U'
boltLauncher = "flatpak run com.adamcake.Bolt"
vesktop = "/opt/Vesktop/vesktop %U"
gpick = "gpick --pick"
gemini = "brave-browser-stable --app=https://gemini.google.com/app"
steam = "steam"
github = "github-desktop"
code = "code-oss"
power = "kitty sh /home/array/.config/scripts/power.sh"

@lazy.window.function
def resize_floating_window(window, width: int = 0, height: int = 0):
    window.cmd_set_size_floating(window.width + width, window.height + height)


keys = [
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "return", lazy.spawn(terminal), desc="Launch terminal"),  # kitty
    Key([mod], "b", lazy.spawn(webBrowser), desc="Launch web browser"),  # brave browser
    Key([mod], "n", lazy.spawn(fileExplorer), desc="Launch file explorer"),  # nemo
    Key([mod], "SPACE", lazy.spawn(appLauncher), desc="Launch rofi"),  # rofi
    Key([mod], "j", lazy.spawn(boltLauncher), desc="Launch bolt launcher"),  # bolt launcher
    Key([mod], "m", lazy.spawn(youtubeMusic), desc="Launch youtube music"),  # youtube music
    Key([mod], "c", lazy.spawn(code), desc="Launch vscode"),  # vscode
    Key([mod], "d", lazy.spawn(vesktop), desc="Launch vesktop"),  # vesktop
    #Key([mod], "p", lazy.spawn(prismLauncher), desc="Launch prism launcher"),  # prism launcher
    Key([mod], "x", lazy.spawn(gpick), desc="Launch gpick"),  # gpick
    Key([mod], "s", lazy.spawn(steam), desc="Launch steam"),  # steam
    Key([mod], "g", lazy.spawn(gemini), desc="Launch gemini"),  # gemini
    Key([], "Home", lazy.spawn(screenshotFull), desc="Take a screenshot"),  # flameshot
    Key([mod], "Left", lazy.layout.shrink()),
    Key([mod], "Right", lazy.layout.grow()),
    Key([mod], "r", lazy.layout.reset(), desc="Reset layout to default"),  # Reset the current layout
    # Custom Binds
    Key([mod], "tab", lazy.function(smart_swap), desc="Smart Swap"),  # Custom swap
    # Key([mod], "tab", lazy.layout.swap_main()), # Swap with main
    Key([mod],"f",lazy.window.toggle_fullscreen(),desc="Toggle fullscreen on the focused window",),  # toggle fullscreen
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Logout"),  # logout
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),  # reload qtile
    Key([mod], "q", lazy.window.kill()),  # kill focused window
    Key([mod, "shift"], "f", lazy.window.toggle_maximize(), desc="Toggle maximize"),
    Key([mod], "p", lazy.spawn("rofi -show power-menu -modi power-menu:.config/qtile/scripts/rofi-power-menu"), desc="Rofi power-menu"),  # kill focused window
    Key([mod], "t", lazy.function(switch_theme), desc="Switch theme"),

    # Audio Binds
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2%"),
        desc="Up the volume",
    ),  # volume up
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -2%"),
        desc="Down the volume",
    ),  # volume down

    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 150+%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5-%")),
    

    Key([mod], "f1", resize_floating_window(width=10), desc="increase width by 10"),
    Key([mod], "f2", resize_floating_window(width=-10), desc="decrease width by 10"),
    Key([mod], "f3", resize_floating_window(height=10), desc="increase height by 10"),
    Key([mod], "f4", resize_floating_window(height=-10), desc="decrease height by 10"),
]

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


group_labels = {
        "1": "",
        "2": "",
        "3": "󰝚",
        "4": "󰵅",
        "5": "󰊖",
        "6": ""
}

groups = [Group(name, label=label) for name, label in group_labels.items()]
for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Move focused window to group {}".format(i.name),
            ),
        ]
    )

layout_conf = {
    'border_focus': current_theme.get("background2"),
    'border_normal': current_theme.get("active"),
    'border_width': 2,
    'margin': 4
}

layouts = [
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Matrix(columns=2, **layout_conf),
    layout.RatioTile(**layout_conf),
]

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                "kitty --class=scratch",
                width=0.5,
                height=0.5,
                x=0.25,
                y=0.20,
                opacity=0.95,
            ),
            DropDown(
                "volume", "pavucontrol", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1
            ),
            DropDown(
                "htop",
                "kitty --class=scratch -e htop",
                width=0.8,
                height=0.8,
                x=0.1,
                y=0.1,
                opacity=1,
            ),
            DropDown(
                "music",
                "kitty --class=scratch -e ncmpcpp",
                width=0.8,
                height=0.8,
                x=0.1,
                y=0.1,
                opacity=1,
            ),
            DropDown(
                "protonmail",
                "brave-browser-stable --app=https://mail.proton.me/u/0/inbox",
                width=0.8,
                height=0.8,
                x=0.1,
                y=0.1,
                opacity=1,
            ),
            DropDown(
                "protondrive",
                "brave-browser-stable --app=https://drive.proton.me/u/0/",
                width=0.8,
                height=0.8,
                x=0.1,
                y=0.1,
                opacity=1,
            ),
        ],
    )
)

# Scratchpad keybindings
keys.extend(
    [
        Key([mod], "v", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key([mod], "o", lazy.group["scratchpad"].dropdown_toggle("volume")),
        Key([mod], "h", lazy.group["scratchpad"].dropdown_toggle("htop")),
        Key([mod, "shift"], "m", lazy.group["scratchpad"].dropdown_toggle("music")),
    ]
)


def longNameParse(text):
    for string in ["Brave", "Code"]:  # Order from longest to shortest
        if string.lower() in text.lower():  # Case-insensitive comparison
            return string  # Return immediately after finding a match
    return text  # Return original text if no match is found

current_layout_icon = widget.CurrentLayoutIcon(
    use_mask=True,
    foreground=current_theme["foreground"],  # Replace with your desired color
    padding=5,
    scale=0.4,
)

qtile = {
    "decorations": [
        RectDecoration(colour="#16181D", radius=3, filled=True, padding_y=4, padding_x=5)
    ],
    "padding": 0,
}

textbox_decor = {
    "decorations": [
        RectDecoration(colour="#16181D", radius=3, filled=True, padding_y=4, padding_x=0)
    ],
    "padding": 14,
}

widget_defaults = dict(
    font="Ubuntu Nerd Font Bold",
    fontsize=13,
    padding=3,
    foreground="#ffffff",
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=12,
                    background=current_theme["background"]
                ),
                widget.TextBox(
                    fmt="  ",
                    fontsize=14,
                    background=current_theme["background"],
                    foreground=current_theme.get("background2"),  # Fallback color
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(appLauncher)},
                ),
                widget.Spacer(length=0, fmt=" ╷ ", background=current_theme["background"]),
                widget.TextBox(fmt=" │ ", foreground=current_theme["foreground"]),
                widget.Spacer(length=0, fmt=" | ", background=current_theme["background"]),
               widget.GroupBox(
                    font="Ubuntu Nerd Font",
                    font_size="14",
                    margin_y=3,
                    margin_x=2,
                    padding_y=5.5,
                    padding_x=5,
                    background=current_theme["background"],
                    active=current_theme["active"],
                    inactive=current_theme["inactive"],
                    rounded=True,
                    highlight_method="block",
                    block_highlight_text_color=current_theme["block_highlight_text_color"],
                    this_screen_border=current_theme["this_screen_border"],
                    this_current_screen_border=current_theme["this_current_screen_border"],
                    urgent_border=current_theme["urgent_border"],
                    urgent_text=current_theme["urgent_text"]
                ),
                widget.Spacer(length=0, fmt=" ╷ ", background=current_theme["background"]),
                widget.TextBox(fmt=" │ ", foreground=current_theme["foreground"]),
                widget.Spacer(length=4, fmt=" | ", background=current_theme["background"]),
                widget.WindowName(
                    format="  {name}",
                    parse_text=longNameParse,
                    background=current_theme["background"],
                    foreground=current_theme["foreground"],
                    max_chars=150,
                ),
                current_layout_icon, 
               widget.CurrentLayout(foreground=current_theme["foreground"], padding_y=20),
                widget.Spacer(length=4, fmt=" ╷ ", background=current_theme["background"]),
                widget.TextBox(fmt=" │ ", foreground=current_theme["foreground"]),
                widget.Spacer(length=8, fmt=" | ", background=current_theme["background"]),
                
                widget.ThermalSensor(tag_sensor='Core 0', format='  {temp:.0f}{unit}', background=current_theme["background"], foreground=current_theme["foreground"]),
                widget.Spacer(length=4, fmt=" ╷ ", background=current_theme["background"]),
                widget.TextBox(fmt=" │ ", foreground=current_theme["foreground"]),
                widget.Spacer(length=8, fmt=" | ", background=current_theme["background"]),
                widget.Memory(format='  {MemUsed: .0f}{mm}', background=current_theme["background"], foreground=current_theme["foreground"]),
                widget.Spacer(length=4, fmt=" ╷ ", background=current_theme["background"]),
                widget.TextBox(fmt=" │ ", foreground=current_theme["foreground"]),
                widget.Spacer(length=8, fmt=" | ", background=current_theme["background"]),
                widget.CheckUpdates(
                        distro='Void', 
                        display_format='    {updates}', 
                        no_update_string = f'<span foreground="{current_theme["foreground"]}">    0</span>',
                        update_interval=60,
                        background=current_theme["background"], 
                        foreground=current_theme["foreground"], 
                ),
                widget.Spacer(length=4, fmt=" ╷ ", background=current_theme["background"]),
                widget.TextBox(fmt=" │ ", foreground=current_theme["foreground"]),
                widget.Spacer(length=8, fmt=" | ", background=current_theme["background"]),
                widget.Volume(
                    fmt="  {}",
                    background=current_theme["background"],
                    foreground=current_theme["foreground"],
                ),
                widget.Spacer(length=4, fmt=" ╷ ", background=current_theme["background"]),
                widget.TextBox(fmt=" │ ", foreground=current_theme["foreground"]),
                widget.Spacer(length=4, fmt=" | ", background=current_theme["background"]),
                widget.WidgetBox(fmt="󱑆 ", foreground=current_theme["foreground"], close_button_location="right", text_open="  ", text_close="  ", widgets=[
                        widget.Systray(
                        background=current_theme["background"],
                        icon_size=19,
                        padding=4),]),
                widget.Clock(
                    format="%a,  %d  -  %H:%M ",
                    foreground=current_theme["foreground"],
                    background=current_theme["background"],
                 ),
                widget.Spacer(
                    length=20,
                    background=current_theme["background"]
                ),
            ],
            38,
            background=current_theme["background"],
            opacity=1.0,
            margin=[4, 4, 0, 4],
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
    border_width=0,
    border_focus="#3A3A3A",
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),
        Match(wm_class="feh"),
        Match(wm_class=["net-runelite-client-RuneLite", "net-runelite-client-RuneLite"]),  
        Match(wm_class=["electron", "Electron"]),       # gitk
    ],
)

auto_fullscreen = True
focus_on_window_activation = "never"
reconfigure_screens = True
auto_minimize = True
os.system("bash ~/.config/qtile/autostart.sh")
wmname = "qtile"
