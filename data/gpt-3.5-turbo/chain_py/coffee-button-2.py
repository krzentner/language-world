# Steps:
    #  1. Line up the gripper with the button
    #  2. Push the button
    # We don't have any specific instructions on how to interact with the coffee
    # machine, so we'll assume that the gripper can easily reach the button.
    # Line up the robot's gripper with the button.
    if check("the robot's gripper is not aligned with the coffee machine button"):
        robot.move("gripper to coffee button")
    # Now that the gripper is lined up, just push the button.
    if check("the robot's gripper is aligned with the coffee machine button"):
        robot.push("coffee button")