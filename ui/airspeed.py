import raylibpy as rl
from ui.colors import light, dark


def draw_marker():
    width, height = rl.get_screen_width(), rl.get_screen_height()
    vertex1 = rl.Vector2(width // 6 - 10, height // 2 + 25)
    vertex2 = rl.Vector2(width // 6 - 10, height // 2 - 25)
    vertex3 = rl.Vector2(width // 6 - 40, height // 2)

    rl.draw_triangle(vertex1, vertex2, vertex3, rl.YELLOW)


def draw_speed_markers_x10(speed, width, height):
    start_value = 0
    step = 5
    max_value = 500
    spacing = 50
    y_position = height // 2 - 15 + 10 * speed

    for i in range(start_value, max_value + 1, step):
        color = rl.YELLOW if speed == i else rl.WHITE

        if i % 5 == 0 and i != 0 and i % 10 != 0:
            rl.draw_line(0, y_position + 10, width // 12 + 30, y_position + 10, color)
        else:
            rl.draw_text(str(i), width // 14, y_position, 28, color)

        y_position -= spacing


def draw_speed_markers_x1(speed, width, height):
    start_value = 0
    step = 1
    max_value = 500
    spacing = 10
    y_position = height // 2 - 15 + 10 * speed

    for i in range(start_value, max_value + 1, step):
        color = rl.YELLOW if speed == i else rl.WHITE

        if i != 0 and i % 10 != 0 and i % 5 != 0:
            rl.draw_line(0, y_position + 10, width // 18, y_position + 10, color)

        y_position -= spacing


def draw_airspeed(speed):

    # Background ---------------------------------------------
    width, height = rl.get_screen_width(), rl.get_screen_height()
    color = rl.Color(10, 10, 18, 255)
    rl.draw_rectangle(0, 0, width // 6, height, color)

    # -----------------------------------------------------------
    draw_marker()
    # -----------------------------------------------------------

    # Speed markers x10  ----------------------------------------
    draw_speed_markers_x10(speed, width, height)

    # Speed markers units ---------------------------------------
    draw_speed_markers_x1(speed, width, height)

    # -----------------------------------------------------------

    rl.draw_text(f"Vel: {speed} kn", 10, height - 25, 24, rl.YELLOW)