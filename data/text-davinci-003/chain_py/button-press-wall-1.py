
    # Steps:
    #  1. Put gripper open and left of the button
    #  2. Line up gripper with short wall and the button
    #  3. Push against the short wall pushing the button
    # First, we need to move the gripper to the left of the button.
    if check("the robot's gripper is not left of the button"):
        robot.put("gripper left of button")
    # Next, move the gripper to the right, being careful not to go too far and
    # catch the wall.
    if check("the robot's gripper is not right of the button and robot's gripper is not left of the wall"):
        robot.move("gripper to right of button")
    # We need to be extra sure now that the gripper is only next to the short
    # wall and not behind it, so we can line up the gripper with the wall.
    if check("the robot's gripper is right of the button and robot's gripper is left of the wall"):
        robot.align("gripper to wall")
    # Push against the short wall, pushing the button.
    if check("the robot's gripper is forward aligned with the short wall and the robot's gripper is behind the button"):
        robot.push("against the wall, pushing the button")