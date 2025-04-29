import os
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen, Rule
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, RectDecoration
from themes.theme import current_theme, switch_theme 
from functions import smart_swap, float_all_windows, tile_all_windows, resize_floating_window, toggle_floating_all

mod = "mod4"
terminal = f"kitty --config /home/array/.config/kitty/{current_theme['kitty_theme']}"
webBrowser = "floorp"
fileExplorer = "thunar"
appLauncher = "rofi -show drun"
screenshotFull = "flameshot full --clipboard --path /home/array/Pictures/Screenshots"
screenshotRegion = "flameshot gui --clipboard --path /home/array/Pictures/Screenshots --accept-on-select"
prismLauncher = "prismlauncher"
youtubeMusic = '/opt/YouTube-Music/youtube-music'
boltLauncher = "dbus-run-session env _JAVA_AWT_WM_NONREPARENTING=1 flatpak run com.adamcake.Bolt"
vesktop = "/opt/Vesktop/vesktop %U"
gpick = "gpick --pick"
steam = "bash .config/qtile/scripts/steam.sh"
code = "code"
nvim = f"kitty --config /home/array/.config/kitty/{current_theme['kitty_theme']} nvim" 
clipboard = "rofi -modi 'clipboard:greenclip print' -show clipboard -run-command 'echo {cmd} | xclip -selection clipboard'"
lock = "betterlockscreen -l blur"

keys = [
    # Program Launchers
    Key([mod], "return", lazy.spawn(terminal), desc="Launch terminal"),  
    Key([mod], "b", lazy.spawn(webBrowser), desc="Launch web browser"),  
    Key([mod], "n", lazy.spawn(fileExplorer), desc="Launch file explorer"),  
    Key([mod], "SPACE", lazy.spawn(appLauncher), desc="Launch app launcher (rofi)"),
    Key([mod], "j", lazy.spawn(boltLauncher), desc="Launch bolt launcher"), 
    Key([mod], "m", lazy.spawn(youtubeMusic), desc="Launch YouTube Music"), 
    Key([mod], "c", lazy.spawn(code), desc="Launch VSCode"),  
    Key([mod], "d", lazy.spawn(vesktop), desc="Launch Vesktop"),
    Key([mod], "x", lazy.spawn(gpick), desc="Launch Gpick color picker"),
    Key([mod], "s", lazy.spawn(steam), desc="Launch Steam"),  
    Key([mod], "l", lazy.spawn(nvim), desc="Launch Neovim"),
    Key([mod], "k", lazy.spawn(clipboard), desc="Launch clipboard manager"),
    Key([mod], "F11", lazy.spawn("bash /home/array/Documents/QtileDots/qtile/scripts/cycle-aio.sh"), desc="Cycle AIO mode"),
    Key([mod], "z", lazy.spawn(lock), desc="Lock Screen"),
    # Screenshots
    Key([], "Home", lazy.spawn(screenshotFull), desc="Take full screenshot"),
    Key([mod], "Home", lazy.spawn(screenshotRegion), desc="Take region screenshot"), 

    # Window Management
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Logout / Quit Qtile"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "tab", lazy.function(smart_swap), desc="Smart swap with master"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Left", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod], "Right", lazy.layout.grow(), desc="Grow window"),
    Key([mod], "r", lazy.layout.reset(), desc="Reset layout"),

    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Layout Management
    Key([mod], "period", lazy.next_layout(), desc="Switch to next layout"),
    Key([mod], "comma", lazy.prev_layout(), desc="Switch to previous layout"),

    # Floating / Tiling Helpers
    Key([mod, "shift"], "space", toggle_floating_all(), desc="Toggle float/tile for all windows"),
    Key([mod], "f", float_all_windows(), desc="Set all windows to floating"),
    Key([mod], "t", tile_all_windows(), desc="Set all windows to tiled"),

    # Theme switching
    Key([mod, "shift"], "t", lazy.function(switch_theme), desc="Switch theme"),

    # Audio Binds
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2%"), desc="Up the volume"),  
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -2%"), desc="Down the volume"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-mute @DEFAULT_AUDIO_SINK@ toggle"), desc="Toggle mute"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 150+%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5-%")),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

group_labels = {
    "1": "",
    "2": "",
    "3": "󰝚",
    "4": "󰵅",
    "5": "󰊖",
    "6": "",
}

groups = [Group(name, label=label) for name, label in group_labels.items()]
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False), desc=f"Move focused window to group {i.name}"),
    ])

layout_conf = {
    'border_focus': current_theme.get("background2"),
    'border_normal': current_theme.get("active"),
    'border_width': 2,
    'margin': 6
}

layouts = [
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.MonadThreeCol(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.RatioTile(**layout_conf),
    layout.Spiral(**layout_conf)
]

groups.append(ScratchPad("scratchpad", [
    DropDown("term", f"kitty --class=scratch --config /home/array/.config/kitty/{current_theme['kitty_theme']}", width=0.5, height=0.5, x=0.25, y=0.20, opacity=1.0),
    DropDown("nvim", f"kitty --class=scratch --config /home/array/.config/kitty/{current_theme['kitty_theme']} sh -c 'nvim'", width=0.6, height=0.6, x=0.2, y=0.15, opacity=1.0),
    DropDown("ytmusic", youtubeMusic, width=0.7, height=0.5, x=0.15, y=0.25, opacity=1.0),
]))

keys.extend([
    Key([mod], "v", lazy.group["scratchpad"].dropdown_toggle("term")),
    Key([mod], "h", lazy.group["scratchpad"].dropdown_toggle("nvim")),
    Key([mod, "shift"], "m", lazy.group["scratchpad"].dropdown_toggle("ytmusic")),
])

def longNameParse(text):
    for string in ["Brave", "Code", "Floorp", "Discord"]:  
        if string.lower() in text.lower():  
            return string  
    return text 

current_layout_icon = widget.CurrentLayoutIcon(
    use_mask=True,
    foreground=current_theme["foreground"],  
    padding=5,
    scale=0.4,
)

widget_defaults = dict(
    font="Ubuntu Nerd Font Bold",
    fontsize=12,
    padding=3,
    background=current_theme["background"],  
    foreground=current_theme["foreground"],
)

extension_defaults = widget_defaults.copy()

separator = lambda: widget.TextBox(fmt=" • ", **widget_defaults)
spacer = lambda length: widget.Spacer(length=length, **widget_defaults)

screens = [
    Screen(
        top=bar.Bar(
            [
                spacer(12),
                widget.GroupBox(
                    font="Ubuntu Nerd Font", font_size="12", margin_y=3, margin_x=2, padding_y=5.3, padding_x=5.2, disable_drag=True,
                    active=current_theme["active"], inactive=current_theme["inactive"], rounded=True,
                    highlight_method="block", block_highlight_text_color=current_theme["block_highlight_text_color"],
                    this_screen_border=current_theme["this_screen_border"], this_current_screen_border=current_theme["this_current_screen_border"],
                    urgent_border=current_theme["urgent_border"], urgent_text=current_theme["urgent_text"],
                ),
                                widget.WindowName(format="  {name}", parse_text=longNameParse, max_chars=150),
                widget.Spacer(),
                widget.Clock(format="%a,  %d      %H:%M"),
                widget.Spacer(),
                current_layout_icon,
                widget.CurrentLayout(padding_y=20),
                separator(),
                widget.ThermalSensor(tag_sensor='Core 0', format='  {temp:.0f}{unit}'),
                separator(),
                widget.Memory(format='  {MemUsed: .0f}{mm}'),
                separator(),
                widget.Volume(fmt="  {}"),
                widget.WidgetBox(fmt=" • ", text_open="  ", text_close="  ", close_button_location="right", widgets=[widget.Systray(icon_size=16, padding=4, fmt=' {} ')]),

                widget.GenPollText(
                update_interval=2,
                func=lambda: subprocess.check_output(
                    ["bash", "-c", "pactl get-source-volume alsa_input.usb-Generic_Blue_Microphones_LT_2102021247069D0112DE_111000-00.analog-stereo | grep -oP '\\d+%' | head -1"]).decode("utf-8").strip(),
                mouse_callbacks={
                    "Button4": lambda: subprocess.Popen([
                        "pactl", "set-source-volume",
                        "alsa_input.usb-Generic_Blue_Microphones_LT_2102021247069D0112DE_111000-00.analog-stereo",
                        "+2%"
                    ]),
                    "Button5": lambda: subprocess.Popen([
                        "pactl", "set-source-volume",
                        "alsa_input.usb-Generic_Blue_Microphones_LT_2102021247069D0112DE_111000-00.analog-stereo",
                        "-2%"
                    ]),
                    "Button3": lambda: subprocess.Popen([
                        "pactl", "set-source-mute",
                        "alsa_input.usb-Generic_Blue_Microphones_LT_2102021247069D0112DE_111000-00.analog-stereo",
                        "toggle"
                    ]),
                },
                fmt=" {}",
            ),

                spacer(12),
            ],
            34,
            background=current_theme["background"],
            opacity=1.0,
            margin=[6, 8, -2, 8]
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
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),
        Match(wm_class="feh"),
    ],
)

import subprocess
subprocess.Popen(['bash', '/home/array/.config/qtile/autostart.sh'])

auto_fullscreen = True
focus_on_window_activation = "never"
reconfigure_screens = True
auto_minimize = True
wmname = "qtile"
