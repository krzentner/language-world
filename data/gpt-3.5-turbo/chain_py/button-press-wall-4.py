# Steps:
    #  1. Put gripper to the side of the wall
    #  2. Move gripper forward, past the wall
    #  3. Line up gripper with button
    #  4. Push down on the button
    # The wall is in the way, so we need to move the gripper to the side of the
    # wall first.
    if check("the gripper is not to the side of the wall"):
        robot.move("gripper to the side of the wall")
    # Once the gripper is to the side of the wall, move the gripper forward until
    # it is past the wall.
    if check("the gripper is to the side of the wall and not past the wall"):
        robot.move("gripper past the wall")
    # Now that the gripper is past the wall, line it up with the button.
    if check("the gripper is past the wall and not vertically aligned with button"):
        robot.put("gripper in front of button")
    # Once the gripper is lined up with the button, just push down on the button.
    if check("the gripper is vertically aligned with button"):
        robot.push("down on button")