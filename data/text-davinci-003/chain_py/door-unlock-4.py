
    # Steps:
    #  1. Put gripper above the dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial to the right order
    # We need to put the gripper above the dial before we can grab it.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    # Now that the gripper is lined up above the dial, we should be able to grab
    # the dial by moving the gripper down to it.
    if check("the robot's gripper is vertically aligned with the dial and the robot's gripper is not around the dial"):
        robot.drop("gripper around dial")
    # Once the dial is grabbed, rotate it to the specified position.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial to the right order")