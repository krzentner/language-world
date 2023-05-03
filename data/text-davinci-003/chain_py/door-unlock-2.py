
    # Steps:
    #  1. Put gripper above dial
    #  2. Drop gripper around dial
    #  3. Pull gripper down and turn dial in the correct direction
    # Put the robot's gripper above the door dial to start.
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.put("the gripper above the dial")
    # If the gripper isn't line up with the dial yet, try to get it closer to the
    # dial by lowering the gripper.
    if check("the robot's gripper is not around dial and the robot's gripper is open"):
        robot.drop("gripper around dial")
    # If the gripper is aligned with the dial and is not near it, close the
    # gripper, trapping the dial and preparing to turn it.
    if check("the robot's gripper is forward aligned with dial and the robot's gripper is not near dial"):
        robot.close("gripper around dial")
    # If the gripper is near the dial, turn it in the correct direction.
    if check("the robot's gripper is near dial"):
        robot.turn("dial in correct direction")