# Steps:
    #  1. Put gripper in front of the button
    #  2. Push the button down
    # First, put the gripper in front of the button.
    if check("the robot's gripper is not in front of the coffee machine button"):
        robot.move("gripper to coffee machine button")
    # Once the gripper is in front of the button, push it down.
    if check("the robot's gripper is in front of the coffee machine button"):
        robot.push("coffee machine button")