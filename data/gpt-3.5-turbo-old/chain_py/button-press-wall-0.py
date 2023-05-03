# Steps:
    #  1. Turn gripper sideways to fit through gap in wall
    #  2. Move gripper towards button
    #  3. Line up gripper with button
    #  4. Push the button
    # To start, turn the gripper sideways so it can fit through the gap in the wall.
    if check("the gripper is not sideways and there is a wall blocking the gripper's path to the button"):
        robot.turn("gripper sideways")
    # Once the gripper is sideways and can fit through the gap in the wall, move
    # the gripper towards the button.
    if check("the gripper is sideways and is not near the button"):
        robot.move("gripper towards button")
    # When the gripper is close, line it up with the button.
    if check("the gripper is near the button and is not vertically aligned with the button"):
        robot.put("gripper in line with button")
    # Finally, push the button.
    if check("the gripper is vertically aligned with the button"):
        robot.push("button")