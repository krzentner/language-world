
    # Steps:
    #  1. Put the gripper below the door handle
    #  2. Push the door handle to close the door
    # If the gripper isn't below the door handle, move it below it.
    if check("the robot's gripper is not below the door handle and the robot's gripper is not near the door handle"):
        robot.put("the gripper below the door handle")
    # If the gripper is around the door handle but the door isn't closed, push
    # harder.
    if check("the robot's gripper is near the door handle and the door is not closed"):
        robot.push("the door closed")

# drawer-close: push the drawer closed to the target location
def drawer_close(robot):
    # Steps:
    #  1. Put the gripper below the drawer handle
    #  2. Push the drawer handle to close the drawer
    # If the gripper isn't below the drawer handle, move it below it.
    if check("the robot's gripper is not below the drawer handle and the robot's gripper is not near the drawer handle"):
        robot.put("the gripper below the drawer handle")
    # If the gripper is around the drawer handle but the drawer isn't closed,
    # push harder.
    if check("the robot's gripper is near the drawer handle and the drawer is not closed"):
        robot.push("the drawer closed")

# window-open: slide the window open to the target location
def window_open(robot):
    # Steps:
    #  1. Put gripper above window handle
    #  2. Slide window open
    # If the robot's gripper isn't above the window handle, move it above.
    if check("the robot's gripper is not above window handle"):
        robot.put("gripper above window handle")
    # If the gripper is above the window handle, slide the window open by moving
    # the gripper left.
    if check("the robot's gripper is above window handle"):
        robot.slide("window left")

# window-close: slide the window closed to the target location
def window_close(robot):
    # Steps:
    #  1. Put gripper above window handle
    # 