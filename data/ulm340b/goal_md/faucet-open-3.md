
"""


instructions_for_step_type = {
    'window-close': {'step_name': 'push', 'step_type': 'push', 'instructions': '\n    Steps:  1. Put gripper left of the window handle  2. Start pushing against the window handle to close the window  3. Push the window closed harder'},
    'peg-insert-side': {'step_name': 'peg-insert-side', 'step_type': 'peg-insert-side', 'instructions': '\n    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg sideways into the hole'},
    'button-press-topdown': {'step_name': 'press', 'step_type': 'press', 'instructions': '\n    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top'},
    'door-open': {'step_name': 'grasp', 'step_type': 'grasp', 'instructions': '\n    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull open the door'},
    'push': {'step_name': 'push', 'step_type': 'push', 'instructions': '\n    Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck to goal'},
    'window-open': {'step_name': 'push', 'step_type': 'push', 'instructions': '\n    Steps:  1. Put gripper right of the window handle  2. Start pushing against the window handle to open the window  3. Push the window open harder'},
    'pick-place': {'step_name': 'pick-place', 'step_type': 'pick-place', 'instructions': '\n    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Move puck to goal'},
    'drawer-open': {'step_name': 'grasp', 'step_type': 'grasp