# Steps:
    #  1. Line up the gripper with the button from above, using sensors to detect the wall
    #  2. Move the robot's arm over the wall
    #  3. Lower the gripper onto the button
    #  4. Push down on the button from the top
    # To line up the gripper with the button from above, we need to detect the presence and location of the wall.
    if check("the robot's sensors detect a wall in the way and the gripper is not lined up with the button"):
        robot.detect_wall("to line up the gripper with the button")
    # After lining up the gripper, move the robot's arm over the wall to reach the button.
    if check("the gripper is lined up with the button and the robot's arm is not over the wall"):
        robot.move_over_wall("to lower the gripper onto the button")
    # Lower the gripper onto the button.
    if check("the gripper is positioned over the button and the gripper is not lowered"):
        robot.lower("the gripper onto the button")
    # Push down on the button.
    if check("the gripper is holding the button"):
        robot.push("down on the button")