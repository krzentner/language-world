

    # Steps:
    #  1. Put gripper near button
    #  2. Line up the gripper with the button
    #  3. Push down on the button
    if check("the robot's gripper is not near the button"):
        robot.move("gripper to button")
    if check("the robot's gripper is not forward aligned with button"):
        robot.put("gripper near button")
    if check("the robot's gripper is forward aligned with button"):
        robot.push("down on button")