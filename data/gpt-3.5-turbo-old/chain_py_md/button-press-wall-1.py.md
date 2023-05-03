# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    # Steps:
    #  1. Put the gripper above the button
    #  2. Move the gripper back to avoid the wall
    #  3. Move the gripper forward to the button
    #  4. Push down on the button
    # First, align the gripper above the button
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Check if a wall is in the way
    if check("there is a short wall between the robot's gripper and button"):
        # Move the gripper back to give it space to move forward
        if check("the robot's gripper is not far from the wall"):
            robot.move("gripper back")
        # Move the gripper forward to the button
        if check("the robot's gripper is not near the button"):
            robot.move("gripper forward")
    # Push down on the button
    if check("the robot's gripper is near the button"):
        robot.push("down on button")