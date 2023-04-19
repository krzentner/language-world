
    # Steps:
    #  1. Put gripper near the button
    #  2. Push the button
    # If the robot's gripper is not near the button on the coffee machine, move
    # the gripper near it.
    if check("the robot's gripper is not near the button"):
        robot.move("gripper to button")
    # If the gripper is near the button, just push it.
    if check("the robot's gripper is near the button"):
        robot.push("button")