
    # Steps:
    #  1. Move gripper near button
    #  2. Line up the gripper as viewed from the front
    #  3. Push the button
    # First, move the gripper near the button.
    if check("the robot's gripper is not near the button"):
        robot.move("gripper near button")
    # Now line up the gripper with the button as seen from the front.
    if check("the robot's gripper is not forward aligned with button"):
        robot.put("gripper forward aligned with button")
    # Now we can finally press the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("button")