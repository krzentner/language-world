# Steps:
    #  1. Put gripper below the handle
    #  2. Grab the handle with the gripper
    #  3. Pull the handle up from the side
    # First, put the gripper below the handle.
    if check("the robot's gripper is not below the handle"):
        robot.move_gripper("below the handle")
    # If the gripper is below the handle, grab it.
    if check("the robot's gripper is below the handle and the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle")
    # After grabbing the handle, we need to pull it up from the side.
    # Check that the gripper is not above the handle and the handle is not in
    # front of the gripper to ensure we are pulling the handle from the side.
    if check("the robot's gripper is below the handle and the handle is not in front of the gripper"):
        robot.move_gripper("above the handle", close_gripper=True)
        robot.move_gripper("to the side of the handle")