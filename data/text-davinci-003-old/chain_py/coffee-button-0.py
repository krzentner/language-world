
    # Steps:
    #  1. Put gripper above the button
    #  2. Drop gripper around the button
    #  3. Push down on the button
    # First, put the gripper above the button, so that we don't accidentally
    # bump it while trying to get it.
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # Once the gripper is lined up above the button, drop it around the button
    # to grab it.
    if check("the robot's gripper is above the button and the robot's gripper is not around button"):
        robot.drop("gripper around button")
    # Once we have the button, just push down on it.
    if check("the robot's gripper is around the button"):
        robot.push("down on button")