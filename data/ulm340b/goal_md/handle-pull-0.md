
We need to figure out the steps the robot should perform to pull up the handle.
"""


#######################################################################################################################


if __name__ == "__main__":
    task_name = "peg-insert-side"
    tutorial_mode = True
    if len(sys.argv) >= 2:
        task_name = sys.argv[1]
    if len(sys.argv) >= 3 and sys.argv[2] == '-t':
        tutorial_mode = True

    if task_name == 'door-close':
        env = door_close()
        if tutorial_mode:
            tutorial(env)

    elif task_name == 'drawer-close':
        env = drawer_close()
        if tutorial_mode:
            tutorial(env)

    elif task_name == 'button-press-topdown':
        env = button_press_topdown()
        if tutorial_mode:
            tutorial(env)

    elif task_name == 'reach':
        env = reach()
        if tutorial_mode:
            tutorial(env)

    elif task_name == 'push':
        env = push()
        if tutorial_mode:
            tutorial(env)

    elif task_name == 'window-close':
        env = window_close()
        if tutorial_mode:
            tutorial(env)

    elif task_name == 'window-open':
        env = window_open()
        if tutorial_mode:
            tutorial(env)

    elif task_name == 'pick-place':
        env = pick_place()
        if tutorial_mode:
            tutorial(env)

    elif task_name == 'peg-insert-side':
        env = peg_insert_side()
        if tutorial_mode:
            tutorial(env)

    elif task_name == 'door-open':
        env = door_open()
        if tutorial_mode:
            tutorial(env)

    elif task_name == 'drawer-open':
        env = drawer_open()
        if tutorial_mode:
            tutorial(env)

    elif task_name == 'handle-pull':
        env = handle_pull()
        if tutorial_mode:
            tutorial(env)

    elif task_name == 'handle-press':
        env = handle_press()
        if tutorial_mode:
            tutorial(env)