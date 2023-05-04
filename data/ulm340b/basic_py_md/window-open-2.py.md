

and then write the lines for the program.
'''.strip()

    if 'window_open' in globals():
        return
    globals()['window_open'] = '''
# window-open: slide the window open to the left
def window_open(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")
'''.strip()

    print(prob)

def do_work(problem, answer):
    work_done = ''
    global HINTS

    if problem == 'door-open':
        global door_open
        work_done = door_open
        if 'drawer_open' in answer:
            HINTS['door-open'] = 2
        if 'button_press_topdown' in answer:
            HINTS['door-open'] = 2
    if problem == 'drawer-open':
        global drawer_open
        work_done = drawer_open
        if 'door_open' in answer:
            HINTS['drawer-open'] = 2
    if problem == 'drawer-close':
        global drawer_close
        work_done = drawer_close
    if problem == 'button-press-topdown':
        global button_press_topdown
        work_done = button_press_topdown
        if 'door_open' in answer:
            HINTS['button-press-topdown'] = 2
        if 'drawer_open' in answer:
            HINTS['button-press-topdown'] = 2
        if 'drawer_close' in answer:
            HINTS['button-press-topdown'] = 2
    if problem == 'peg-insert-side':
        global peg_insert_side
        work_done = peg_insert_side
        if 'door_open' in answer:
            HINTS['peg-insert-side'] = 2
        if 'button_press_topdown' in answer:
            HINTS['peg-insert-side'] = 2
        if 'drawer_open' in answer: