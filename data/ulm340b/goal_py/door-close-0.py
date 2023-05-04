
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door handle is
    # large and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the door is aligned with the gripper as seen from in front, we can
    # push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.move_gripper("vertically aligned with door handle")

# door-open-from-behind: push the door open from behind
def door_open_from_behind(robot):
    # Steps:
    #  1. Put gripper behind the door handle
    #  2. Push the door open
    # First, put the gripper roughly behind the door handle.
    if check("the robot's gripper is not behind the door handle"):
        robot.move_gripper("behind the door handle")
    # If the gripper is behind the door handle, we can push it open.
    if check("the robot's gripper is behind the door handle and the robot's gripper is below the door handle"):
        robot.move_gripper("vertically aligned with door handle")

# drawer-open-from-side: push the drawer open from the side
def drawer_open_from_side(robot):
    # Steps:
    #  1. Put gripper roughly to the right of the drawer handle
    #  2. Push the drawer open
    # First, put the gripper roughly to the right of the drawer handle.
    if check("the robot's gripper is not behind the drawer handle"):
        robot.move_gripper("behind the drawer handle")
    # Once the gripper is in roughly the correct place, we can push the drawer
    # open.
    if check("the robot's gripper is behind the drawer handle and the robot's gripper is below the drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")

# drawer-close