
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull up on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the handle becomes left of the gripper, go back to putting the gripper
    # above the handle.
    if check("the handle is not left of the robot's gripper and the handle is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the handle", close_gripper=True)
    # As long the gripper is still mostly around the handle, pull up on the
    # handle.
    if check("the robot's gripper is forward aligned with the handle"):
        robot.move_gripper("above the handle")