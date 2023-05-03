# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put gripper around the handle
    #  2. Rotate the handle up
    # Before we can rotate the lever we need to put the gripper around the handle.
    if check("the robot's gripper is not around the lever handle"):
        robot.move_gripper("around the lever handle")
    # Once the gripper is around the handle, we can rotate the lever.
    # We'll rotate the lever until it's at the maximum angle, which we'll assume
    # to be 90 degrees.
    if check("the robot's gripper is around the lever handle"):
        robot.move_gripper("maximally rotated up")