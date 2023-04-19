# Steps:
    # 1. Move the gripper near the button and the wall
    # 2. Rotate the gripper so that it is vertical and facing the wall
    # 3. Push the gripper towards the button and wall to press the button
    # To press the button while avoiding the wall, we need to rotate the gripper
    # first so that it faces the wall.
    if check("the robot's gripper is not near button and the wall"):
        robot.move_gripper("near the button and the wall")
    # Once the gripper is near the button and the wall, rotate the gripper so that
    # it's facing the wall.
    if check("the robot's gripper is not facing the wall"):
        robot.rotate_wrist("facing the wall")
    # Now, move the gripper towards the button and wall to press the button.
    if check("the robot's gripper is facing the wall"):
        robot.move_gripper("touching the button and wall")