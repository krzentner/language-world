# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Close drawer by pushing it
    # We need to put the gripper above the drawer handle before we can close it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    # Once the gripper is lined up above the drawer handle, we can push the drawer
    # closed by moving the gripper to the left (since we're assuming the drawer
    # is on the right side of the robot).
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.push("drawer right")