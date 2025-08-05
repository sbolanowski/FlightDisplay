import raylibpy as rl
from ui.colors import light, dark


def draw_marker():
    width, height = rl.get_screen_width(), rl.get_screen_height()
    vertex1 = rl.Vector2(width - width // 6 + 10, height // 2 - 25)
    vertex2 = rl.Vector2(width - width // 6 + 10, height // 2 + 25)
    vertex3 = rl.Vector2(width - width // 6 + 40, height // 2)

    rl.draw_triangle(vertex1, vertex2, vertex3, rl.BLUE)


def draw_altimeter_markers_x10(alt, width, height):
    start_value = 0
    step = 5
    max_value = 500
    spacing = 50
    y_position = height // 2 - 15 + 10 * alt

    for i in range(start_value, max_value + 1, step):
        color = rl.BLUE if alt == i else rl.WHITE

        if i % 5 == 0 and i != 0 and i % 10 != 0:
            rl.draw_line(width - width // 12 - 30, y_position + 10, width, y_position + 10, color)
        else:
            rl.draw_text(str(i * 10), width - width // 10 - 15, y_position, 28, color)

        y_position -= spacing


def draw_altimeter_markers_x1(alt, width, height):
    start_value = 0
    step = 1
    max_value = 500
    spacing = 10
    y_position = height // 2 - 15 + 10 * alt

    for i in range(start_value, max_value + 1, step):
        color = rl.BLUE if alt == i else rl.WHITE

        if i != 0 and i % 10 != 0 and i % 5 != 0:
            rl.draw_line(width - width // 18, y_position + 10, width, y_position + 10, color)

        y_position -= spacing


def draw_altimeter(alt):

    # Background ---------------------------------------------
    width, height = rl.get_screen_width(), rl.get_screen_height()
    color = rl.Color(10, 10, 18, 255)
    rl.draw_rectangle(width - width // 6, 0, width // 6, height, color)

    # -----------------------------------------------------------
    draw_marker()
    # -----------------------------------------------------------

    # Speed markers x10  ----------------------------------------
    draw_altimeter_markers_x10(alt, width, height)

    # Speed markers units ---------------------------------------
    draw_altimeter_markers_x1(alt, width, height)

    # -----------------------------------------------------------
    rl.draw_text(f"Alt: {alt * 10} ft", width - 150, height - 25, 24, rl.BLUE)