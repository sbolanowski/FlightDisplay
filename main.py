import raylibpy as rl
import argparse
from ui.artificial_horizon import draw_gradient_background, draw_red_cross
from ui.colors import light, dark
from utils import handle_input

# Global vars ------------------
degrees = 0
mult = 10
max_degree = 90 * mult

test_mode = False
last_time = 0
state = "up"
# ------------------------------

def main(width, height, theme="light"):
    global degrees, max_degree, mult, test_mode, last_time, state

    rl.init_window(width, height, "PFD - Drone testing")
    rl.set_target_fps(60)

    while not rl.window_should_close():

        rl.begin_drawing()
        rl.clear_background(rl.DARKGRAY)

        selected_theme = light if theme == "light" else dark
        draw_gradient_background(degrees, selected_theme)
        draw_red_cross()

        # Manejar la entrada de teclas y el test mode con la función `handle_input`
        degrees, test_mode, last_time, state = handle_input(degrees, max_degree, mult, test_mode, last_time, state=state)

        rl.draw_text(f"{int(degrees/mult)} º", 10, 10, 32, rl.YELLOW)

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
