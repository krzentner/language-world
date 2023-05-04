
''')


def get_step_name(idx):
    if idx == 0:
        return "move gripper to right of window handle"
    elif idx == 1:
        return "slide window left"
    elif idx == 2:
        return "push window left harder"
    elif idx == 3:
        return "put gripper above peg"
    elif idx == 4:
        return "grab peg"
    elif idx == 5:
        return "align peg to hole"
    elif idx == 6:
        return "insert peg into hole"
    elif idx == 7:
        return "grab drawer handle"
    elif idx == 8:
        return "push drawer closed"
    elif idx == 9:
        return "put gripper above drawer handle"
    elif idx == 10:
        return "put gripper around drawer handle"
    elif idx == 11:
        return "pull away from drawer"
    elif idx == 12:
        return "put gripper above button"
    elif idx == 13:
        return "push down on button"
    elif idx == 14:
        return "put gripper above door handle"
    elif idx == 15:
        return "put gripper around door handle"
    elif idx == 16:
        return "pull door open"
    elif idx == 17:
        return "place gripper above puck"
    elif idx == 18:
        return "drop gripper around puck"
    elif idx == 19:
        return "close gripper around puck"
    elif idx == 20:
        return "place puck at goal"
    elif idx == 21:
        return "put the gripper above the puck"
    elif idx == 22:
        return "push the gripper into the puck"
    elif idx == 23:
        return "slide the puck to the goal"
    elif idx == 24:
        return "reach to goal"
    elif idx == 25:
        return "move gripper to left of window handle"
    elif idx == 26:
        return "slide window right"
    elif idx == 27:
        return "push window right harder"

    return None


def get_full_step_description(env, idx, params=None):
    if params is None:
        params = {}
    
    # if idx < 28:
    if idx <= 27:
        param_