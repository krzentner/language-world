
    # Steps:
    #  1. Put gripper in front of wall
    #  2. Put short wall between gripper and button
    #  3. Push down on button with wall
    # First, put the gripper in front of the wall.
    if check("the robot's gripper is not in front of wall"):
        robot.put("gripper in front of wall")
    # Now, put the robot's gripper to the side of the button, but with a short
    # wall between the gripper and the button.
    if check("the robot's gripper is not to the side of the button and there is no wall between the gripper and the button"):
        robot.place("wall between gripper and button")
    # If the gripper is to the side of the button and with a wall between them,
    # we can just push down on the button with the wall to press the button.
    if check("the robot's gripper is to the side of the button and there is a wall between the gripper and the button"):
        robot.push("down on button with wall")