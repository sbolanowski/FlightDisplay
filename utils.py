import raylibpy as rl

def handle_input_speed(speed):
    if rl.is_key_pressed(rl.KEY_U):
        speed += 1
    if rl.is_key_pressed(rl.KEY_J):
        if speed > 0:
            speed -= 1
    return speed


def handle_input_altitude(alt):
    if rl.is_key_pressed(rl.KEY_I):
        alt += 1
    if rl.is_key_pressed(rl.KEY_K):
        if alt > 0:
            alt -= 1
    return alt

def handle_input_roll(roll, max_degree):
    # Roll counter-clockwise
    if rl.is_key_pressed(rl.KEY_A):
        if roll > -max_degree:
            roll -= 1
    
    # Roll clockwise
    if rl.is_key_pressed(rl.KEY_D):
        if roll < max_degree:
            roll += 1

    return roll



def handle_input_attitude(degrees, max_degree, mult, test_mode, last_time, time_interval=0.2, state="up"):

    # Reset ------------------------
    if rl.is_key_pressed(rl.KEY_X):
        degrees = 0
    # ------------------------------

    # INVERTED CONTROL! UPWARD -----
    if rl.is_key_pressed(rl.KEY_S):
        if degrees < max_degree:
            degrees += 1 * mult
    # ------------------------------

    # INVERTED CONTROL! DOWNWARD ---
    if rl.is_key_pressed(rl.KEY_W):
        if degrees > -max_degree:
            degrees -= 1 * mult
    # ------------------------------

    # TEST MODE
    if rl.is_key_pressed(rl.KEY_SPACE):
        test_mode = not test_mode

    if test_mode:
        current_time = rl.get_time()

        if current_time - last_time >= time_interval:
            if state == "up":
                if degrees < max_degree:
                    degrees += 1 * mult
                elif degrees == max_degree:
                    state = "down"
            elif state == "down":
                if degrees > -max_degree:
                    degrees -= 1 * mult
                elif degrees == -max_degree:
                    state = "middle"
            elif state == "middle":
                if degrees < 0:
                    degrees += 1 * mult
                elif degrees == 0:
                    test_mode = False
                    state = "up"

            last_time = current_time

    return degrees, test_mode, last_time, state
