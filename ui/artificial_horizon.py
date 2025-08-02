import raylibpy as rl
from ui.colors import light, dark

def draw_red_cross():

    width, height = rl.get_screen_width(), rl.get_screen_height()
    center_x, center_y = width // 2, height // 2
    cross_size = 100
    cross_thickness = 8
    color = rl.MAGENTA

    # Horizontal
    rl.draw_rectangle(center_x - cross_size // 2, center_y - cross_thickness // 2, cross_size, cross_thickness, color)

    # Vertical
    rl.draw_rectangle(center_x - cross_thickness // 2, center_y - cross_size // 2, cross_thickness, cross_size, color)

# ------------------------------

def draw_gradient_background(degrees, theme):

    width, height = rl.get_screen_width(), rl.get_screen_height()
    mult = 2
    extended_height = height * mult
    offset_y = (degrees - (height / mult))

    sky_color_light = theme["sky"]["light"]
    sky_color_dark = theme["sky"]["dark"]
    earth_color_light = theme["earth"]["light"]
    earth_color_dark = theme["earth"]["dark"]

    # Sky
    for i in range(-extended_height, extended_height):

        ratio = (i + extended_height) / (extended_height * 2)

        color = rl.Color(
            int(sky_color_dark[0] + ratio * (sky_color_light[0] - sky_color_dark[0])),
            int(sky_color_dark[1] + ratio * (sky_color_light[1] - sky_color_dark[1])),
            int(sky_color_dark[2] + ratio * (sky_color_light[2] - sky_color_dark[2])),
            255
        )
        rl.draw_line(0, i + offset_y, width, i + offset_y, color)

    # Ground
    for i in range(extended_height // 2, extended_height * 2):

        ratio = ((i - extended_height // 2) / (extended_height // 2))

        color = rl.Color(
            int(earth_color_light[0] + ratio * (earth_color_dark[0] - earth_color_light[0])),
            int(earth_color_light[1] + ratio * (earth_color_dark[1] - earth_color_light[1])),
            int(earth_color_light[2] + ratio * (earth_color_dark[2] - earth_color_light[2])),
            255
        )
        rl.draw_line(0, i + offset_y, width, i + offset_y, color)

    horizon_y = extended_height // 2 + offset_y
    rl.draw_line(0, horizon_y, width, horizon_y, rl.WHITE)

    # ===================================================

    # Markers params
    line_length = 180
    height_separation = 100
    offset = 20

    for i in range(-18, 19):  # x5 Degree marker

        if i < 0 and theme==dark:
            color = rl.BLACK
        else:
            color = rl.WHITE

        y_position = horizon_y + i * (height_separation / 2)
        rl.draw_line(width // 2 - (line_length / 2) // 2, y_position, width // 2 + (line_length / 2) // 2, y_position, color)


    for i in range(-9, 10):  # x10 Degree marker

        if i < 0 and theme==dark:
            color = rl.BLACK
        else:
            color = rl.WHITE

        y_position = horizon_y + i * height_separation
        rl.draw_line(width // 2 - line_length // 2, y_position, width // 2 + line_length // 2, y_position, color)

        if i != 0:  # Print numeric degree
            degree = i * (-10)
            rl.draw_text(str(degree), width // 2 + line_length // 2 + offset, y_position - 10, 24, color)  # Right
            rl.draw_text(str(degree), width // 2 - line_length // 2 - offset - (offset*2), y_position - 10, 24, color) # Left
