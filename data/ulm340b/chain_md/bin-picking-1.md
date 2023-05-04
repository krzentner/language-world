
    Steps:  1. Move robot's gripper above the cube  2. Put gripper around the cube  3. Close gripper around cube  4. Move gripper with cube to above target bin  5. Release the gripper  6. Move gripper back to start position
    Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper near door handle  2. Push the door closed
    If the gripper is not near the door handle, move it to the door handle.
    - When the robot's gripper is not near the door handle, the robot should grab door handle.
    If the drawer is aligned with the gripper as seen from in front, we can push the door closed.
    - When the robot's gripper is forward aligned with door handle, the robot should push door closed.

The task `drawer-close-side` requires the robot to push the drawer closed from the side.
To push the drawer closed from the side reliably, the robot should perform the following steps:
    Steps:  1. Put the robot's gripper left of the drawer handle  2. Push the drawer closed  3. Push the drawer closed harder
    First, we need to move the robot's gripper left of the drawer handle.
    - When the robot's gripper is not left of drawer handle, the robot should move gripper to left of drawer handle.
    If the gripper is left of the drawer handle, move the drawer handle right.
    - When the robot's gripper is left of the drawer handle, the robot should push drawer closed.
    If the gripper is in front of the drawer handle, push it harder.
    - When the robot's gripper is in front of drawer handle, the robot should push drawer right harder.

"""

if __name__ == "__main__":
    sys.path.append(sys.argv[1])
    task_name = sys.argv[2]
    if task_name == "button-press-topdown":
        task_instructions = button_press_topdown_instructions
    elif task_name == "drawer-close":
        task_instructions = drawer_close_instructions
    elif task_name == "door-open":
        task_instructions = door_open_instructions
    elif task_name == "drawer