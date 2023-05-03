# Steps:
    #  1. Put gripper in front of coffee machine button
    #  2. Push the button down
    # We don't need to worry about the direction for this task, so we can just put
    # the gripper in front of the button.
    if check("the robot's gripper is not in front of coffee machine button"):
        robot.move("gripper to button")
    # Push the button down.
    if check("the robot's gripper is in front of coffee machine button"):
        robot.push("coffee machine button down")