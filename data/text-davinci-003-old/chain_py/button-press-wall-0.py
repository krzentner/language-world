
    # Steps:
    #  1. Put gripper in front of wall
    #  2. Lower gripper onto the button until there is contact
    #  3. Push down on the button until it is pressed
    # Put the gripper right in front of the wall so that it aligns with the wall
    # and can push down on the button behind it.
    if check("the robot's gripper is not in front of the wall"):
        robot.put("gripper in front of wall")
    # Lower the gripper until it is touching the button and pushing on it.
    if check("the robot's gripper is above the button and the robot's gripper is in front of the wall"):
        robot.lower("gripper onto button")
    # Now it is making contact, just push harder and the button should press.
    if check("the robot's gripper is touching the button and the robot's gripper is in front of the wall"):
        robot.push("down on button")