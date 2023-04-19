
    # Steps:
    #  1. Line up the robot's gripper as viewed from the side
    #  2. Push down the handle from the side
    # First, put the gripper mostly to the side of the handle.
    if check("the robot's gripper is not almost vertically aligned with the handle"):
        robot.move_gripper("almost vertically aligned with the handle")
    # Now that the gripper is mostly lined up, just press down on the handle.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.move_gripper("to the side of the handle")