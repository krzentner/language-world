```
# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper above the drawer handle
    #  2. Move the gripper to the right to close the drawer
    #  3. Push the drawer close harder
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # Once the gripper is lined up above the drawer handle, we can move the gripper
    # to the right to close the drawer.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not horizontally aligned with the drawer handle"):
        robot.move_gripper("horizontally aligned with the drawer handle")
    # Once the gripper is on the right side of the drawer handle, we can push the
    # drawer close.
    if check("the robot's gripper is right of the drawer handle"):
        robot.move_gripper("left of the drawer handle")