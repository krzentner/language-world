
    # Steps:
    #  1. Put gripper above the dial
    #  2. Drop the gripper around the dial
    #  3. Turn the dial to unlock the door
    # We need to put the robot's gripper above the dial, otherwise we may not be
    # able to grab it.
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.move_gripper("vertically aligned with dialog")
    # Once the gripper is above the dial, close the gripper and turn the dial.
    if check("the robot's gripper is vertically aligned with dial"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Turn the dial until it unlocks the door.
    if check("the robot's gripper is around dial"):
        robot.move_gripper("horizontally aligned with the dial")