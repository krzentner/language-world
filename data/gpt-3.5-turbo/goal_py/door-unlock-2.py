# Steps:
    #  1. Put gripper above dial
    #  2. Drop gripper around dial
    #  3. Turn the dial to unlock the door
    # Put the gripper above the dial.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial")
    # If the gripper is not around the dial yet, put it around the dial by
    # closing the gripper.
    if check("the robot's gripper is not around the dial and the gripper is open"):
        robot.move_gripper("near the dial", close_gripper=True)
    # If the gripper is around the dial we can start turning to unlock the door.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("rotate the dial")