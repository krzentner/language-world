# Steps:
    #  1. Move gripper to the side of the wall
    #  2. Move gripper in front of the button
    #  3. Push the button
    # Because there is a wall in the way, we need to first move the gripper to
    # the side of the wall before we can move it to the button.
    if check("the robot's gripper is not to the side of the wall"):
        robot.move("gripper to side of wall")
    # Once the gripper is to the side of the wall, move it towards the button.
    # We don't need to worry about lining up with the button vertically, since
    # we're pushing it from in front.
    if check("the robot's gripper is not in front of button"):
        robot.move("gripper in front of button")
    # Once the gripper is in front of the button, push the button.
    if check("the robot's gripper is in front of button"):
        robot.push("button")