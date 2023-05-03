
    # Steps:
    #  1. Put gripper above dial
    #  2. Grab dial
    #  3. Turn dial
    # First, put the gripper above the dial to make sure we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.grab("dial from above")
    # Once the gripper is above the dial, grab it and turn it.
    if check("the robot's gripper is vertically aligned with dial"):
        robot.grab("dial")
        robot.turn("dial")