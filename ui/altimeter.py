import raylibpy as rl
from ui.colors import light, dark


def draw_marker():
    width, height = rl.get_screen_width(), rl.get_screen_height()
    vertex1 = rl.Vector2(width - width//6 + 10, height//2 - 25)
    vertex2 = rl.Vector2(width - width//6 + 10, height//2 + 25)
    vertex3 = rl.Vector2(width - width//6 + 35, height//2)

    rl.draw_triangle(vertex1, vertex2, vertex3, rl.DARKBLUE)


def draw_altimeter(alt):

    # Background    ---------------------------------------------
    
    width, height = rl.get_screen_width(), rl.get_screen_height()
    color = rl.Color(10, 10, 18, 255)

    rl.draw_rectangle(width - width//6, 0, width//6, height, color)
    
    # -----------------------------------------------------------
    draw_marker()
    # -----------------------------------------------------------

    # Speed markers   -------------------------------------------

    start_value = 0
    step = 5
    max_value = 500
    spacing = 50

    y_position = height // 2 -15 + 10*alt

    for i in range(start_value, max_value + 1, step):
        if i % 5 == 0 and i != 0 and i % 10 != 0:
            rl.draw_line(width - width // 12 - 40, y_position + 10, width - width // 12 + 30, y_position + 10, rl.WHITE)
        elif alt == i:
            rl.draw_text(str(i*10), width - width // 12 - 20, y_position, 28, rl.DARKBLUE)
        else:
            rl.draw_text(str(i*10), width - width // 12 - 20, y_position, 28, rl.WHITE)

        y_position -= spacing

    # -----------------------------------------------------------

    rl.draw_text(f"Alt: {alt*10} ft", width-150, height-25, 24, rl.DARKBLUE)