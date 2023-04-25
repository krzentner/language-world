
    # Steps:
    #  1. Put gripper left of the wall
    #  2. Push wall to the right
    #  3. Line up the gripper with the button
    #  4. Push the button
    # First, move the gripper to the left of the wall.
    if check("the robot's gripper is not left of wall"):
        robot.move("gripper left of wall")
    # Now that the gripper is to the left of the wall, push the wall to the right
    # until it's out of the way.
    if check("the wall is not right of the robot's gripper and the robot's gripper is near wall"):
        robot.push("wall right")
    # When the wall is out of the way, line up the gripper with the button.
    if check("the wall is right of the robot's gripper and the robot's gripper is not forward aligned with button"):
        robot.align("gripper to button")
    # When the gripper is lined up with the button, push the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("button")