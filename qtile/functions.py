# ~/.config/qtile/my_qtile_functions.py
from libqtile.lazy import lazy

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
