import raylibpy as rl
from ui.colors import light, dark

# Testing vel scroll
speed = 0


def draw_marker():
    width, height = rl.get_screen_width(), rl.get_screen_height()
    vertex1 = rl.Vector2(width//6 - 10, height//2 + 25)
    vertex2 = rl.Vector2(width//6 - 10, height//2 - 25)
    vertex3 = rl.Vector2(width//6 - 35, height//2)

    offset = 3

    for i in range(-offset, offset + 1):
        rl.draw_triangle_lines(
            rl.Vector2(vertex1.x + i, vertex1.y + i),
            rl.Vector2(vertex2.x + i, vertex2.y + i),
            rl.Vector2(vertex3.x + i, vertex3.y + i),
            rl.YELLOW
        )


def draw_airspeed():

    # Testing scroll
    global speed
    if rl.is_key_pressed(rl.KEY_I):
        speed += 1
    if rl.is_key_pressed(rl.KEY_K):
        if speed > 0:
            speed -= 1

    # Background    ---------------------------------------------

    width, height = rl.get_screen_width(), rl.get_screen_height()
    color = rl.Color(10, 10, 18, 255)

    rl.draw_rectangle(0, 0, width // 6, height, color)

    # rec = rl.Rectangle(0 + 10, 0 + 10, width // 6 - 15, height - 15)
    # rl.draw_rectangle_rounded(rec, 0.20, 20, custom_color)

    # -----------------------------------------------------------
    draw_marker()

    # -----------------------------------------------------------

    # Speed markers   -------------------------------------------

    start_value = 0
    step = 5
    max_value = 500
    spacing = 50

    y_position = height // 2 -15 + 10*speed

    for i in range(start_value, max_value + 1, step):
        if i % 5 == 0 and i != 0 and i % 10 != 0:
            rl.draw_line(width // 12 - 40, y_position + 10, width // 12 + 30, y_position + 10, rl.WHITE)
        elif speed == i:
            rl.draw_text(str(i), width // 12 - 20, y_position, 28, rl.YELLOW)
        else:
            rl.draw_text(str(i), width // 12 - 20, y_position, 28, rl.WHITE)

        y_position -= spacing

    # -----------------------------------------------------------

    rl.draw_text(f"Vel: {speed}", 10, height-25, 24, rl.GREEN)