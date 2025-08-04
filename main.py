import raylibpy as rl
import argparse
from ui.artificial_horizon import draw_gradient_background, draw_red_cross
from ui.airspeed import draw_airspeed
from ui.altimeter import draw_altimeter
from ui.colors import light, dark
from utils import handle_input_attitude, handle_input_altitude, handle_input_speed

# Global vars ------------------
alt = 0
speed = 0

degrees = 0
mult = 10
max_degree = 90 * mult

test_mode = False
last_time = 0
state = "up"
# ------------------------------

def main(width, height, theme="light"):
    global alt, speed, degrees, max_degree, mult, test_mode, last_time, state

    rl.init_window(width, height, "PFD - Drone testing")
    rl.set_target_fps(60)

    while not rl.window_should_close():

        rl.begin_drawing()
        rl.clear_background(rl.DARKGRAY)

        selected_theme = light if theme == "light" else dark

        draw_gradient_background(degrees, selected_theme)
        draw_airspeed(speed)
        draw_altimeter(alt)


        # Handle input teleoperated mode ------------
        degrees, test_mode, last_time, state = handle_input_attitude(degrees, max_degree, mult, test_mode, last_time, state=state)
        alt = handle_input_altitude(alt)
        speed = handle_input_speed(speed)
        # --------------------------------------------

        rl.draw_text(f"{int(degrees/mult)} º", 10, 10, 32, rl.MAGENTA)

        rl.end_drawing()

    rl.close()

# ------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parameters...")
    parser.add_argument('--w', type=int, default=1000, help='Width of the window.')
    parser.add_argument('--h', type=int, default=600, help='Height of the window.')
    parser.add_argument('--theme', type=str, default="light", choices=["light", "dark"], help="Choose color theme: 'light' or 'dark'.")

    args = parser.parse_args()

    main(args.w, args.h, args.theme)
