# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    #  1. Put the gripper near the handle
    #  2. Grasp the handle with the gripper
    #  3. Turn the handle up
    # First, put the gripper near the handle
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # Check if the gripper is lined up with the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # After the gripper is aligned with the handle, turn the handle up by rotating
    # the gripper.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.rotate_gripper("up")