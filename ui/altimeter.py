import raylibpy as rl
from ui.colors import light, dark

def draw_altimeter():

    # Background    ---------------------------------------------
    
    width, height = rl.get_screen_width(), rl.get_screen_height()
    color = rl.Color(10, 10, 18, 255)

    rl.draw_rectangle(width - width//6, 0, width//6, height, rl.BLACK)

    rec = rl.Rectangle(width - width//6 + 10, 0 + 10, width//6 - 15, height - 15)
    rl.draw_rectangle_rounded(rec, 0.20, 20, color)

    # -----------------------------------------------------------


