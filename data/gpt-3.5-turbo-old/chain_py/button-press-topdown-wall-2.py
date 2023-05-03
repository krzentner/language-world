# Steps:
    # 1. Move gripper above button
    # 2. Move gripper towards wall
    # 3. Move gripper down to press button
    # 4. Lift gripper back up
    # First, put the gripper roughly above the button
    if check("the robot's gripper is not above the button"):
        robot.place("gripper above button")
    # Move the gripper towards the wall, so that it is in the right position to
    # press the button.
    if check("the gripper is not close to the wall"):
        robot.move("gripper towards the wall")
    # Move the gripper down to press the button.
    if check("the gripper is close to the wall and is not aligned vertically with the button"):
        robot.move("gripper down towards button")
    # Press the button by moving the gripper even further down.
    if check("the gripper is aligned vertically with the button"):
        robot.push("down on the button")
    # Lift the gripper back up after pressing the button.
    if check("the gripper is not back up above the button"):
        robot.lift("gripper back up")