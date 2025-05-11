from libqtile.lazy import lazy
from libqtile import bar, layout, qtile, widget, hook
import datetime

def separator():
    return widget.TextBox(fmt=" ∷ ")

def format_time():
    return datetime.now().strftime("󰥔  %a,  %d   %H:%M %p").replace("am", "AM").replace("pm", "PM")

def smart_swap(qtile):
    layout = qtile.current_layout
    window = qtile.current_window
    if hasattr(layout, "clients") and window in layout.clients:
        index = layout.clients.index(window)
        if index == 0:
            layout.swap_right()
        else:
            layout.swap_main()

@lazy.function
def float_all_windows(qtile):
    for win in qtile.current_group.windows:
        win.floating = True
        win.bring_to_front()

@lazy.function
def tile_all_windows(qtile):
    for win in qtile.current_group.windows:
        win.floating = False  

@lazy.function
def toggle_floating_all(qtile):
    floating = any(win.floating for win in qtile.current_group.windows)
    if floating:
        tile_all_windows(qtile)
    else:
        float_all_windows(qtile)         

@lazy.window.function 
def resize_floating_window(window, width: int = 0, height: int = 0): 
    window.cmd_set_size_floating(window.width + width, window.height + height)

@lazy.function
def update_visible_groups(qtile):
    visible = []
    for group in qtile.groups:
        if group.name in ["6", "7", "8", "9"]:
            # Show only if focused or has windows
            if group == qtile.current_group or group.windows:
                visible.append(group.name)
        else:
            visible.append(group.name)
    for w in qtile.widgets_map.values():
        if hasattr(w, 'visible_groups'):
            w.visible_groups = visible
            w.bar.draw()

@hook.subscribe.client_managed
@hook.subscribe.client_killed
@hook.subscribe.setgroup
def refresh_groups(*_):
    update_visible_groups(qtile)
