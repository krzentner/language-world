# Steps:
    #  1. Move gripper above the button
    #  2. Push the button down
    # First, move the gripper above the button.
    if check("the robot's gripper is not above the coffee machine button"):
        robot.move("gripper to above coffee machine button")
    # Then, push down on the button.
    if check("the robot's gripper is above the coffee machine button"):
        robot.push("down on coffee machine button")