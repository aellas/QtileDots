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

@lazy.window.function 
def resize_floating_window(window, width: int = 0, height: int = 0): 
    window.cmd_set_size_floating(wwindow.width + width, window.height + height)