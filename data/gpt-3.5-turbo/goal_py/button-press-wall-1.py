# Steps:
    # 1. Move gripper to the side of the wall
    # 2. Move gripper forward and around wall to reach button
    # 3. Push in button
    # First, move the gripper to the side of the wall.
    if check("the robot's gripper is not aside of the wall"):
        robot.move_gripper("beside the wall")
    # Once the gripper is beside the wall, move it forward and around the wall
    # to reach the button.
    if check("the robot's gripper is not in front of the wall"):
        robot.move_gripper("in front of the wall")
    if check("the robot's gripper is not around the wall"):
        robot.move_gripper("around the wall")
    # Now that the gripper is around the wall and above the button, push the
    # button.
    if check("the robot's gripper is above the button"):
        robot.move_gripper("near the button")