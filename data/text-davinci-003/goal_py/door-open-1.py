
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # To open the door, we must first line up the gripper with the door handle.
    # This is more difficult than with regular handles as the door handle is at
    # an angle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
    # Now that the gripper is lined up from above, we need to make sure it's
    # lined up horizontally in front of the door handle as well.
    if check("the robot's gripper is not horizontally aligned with the door handle"):
        robot.move_gripper("horizontally aligned with the door handle")
    # Now that it's lined up in front, we can just pull open the door.
    if check("the robot's gripper is horizontally aligned with the door handle"):
        robot.move_gripper("horizontally aligned with the door handle")