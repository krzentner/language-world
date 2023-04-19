
    # Steps:
    #  1. Put gripper above the dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial in the direction desired
    # First, put the gripper above the dial.
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above dial")
    # Once the gripper is roughly above the dial, grab the dial with the robot's
    # gripper.
    if check("the robot's gripper is above the dial and the robot's gripper is open"):
        robot.grab("dial")
    # Once the gripper is fully around the dial, turn the dial in the direction
    # desired.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial in direction desired")