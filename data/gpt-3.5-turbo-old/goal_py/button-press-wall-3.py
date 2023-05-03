# Steps:
    #   1. Move robot to the side of the wall, aligned with the button
    #   2. Move gripper to the front of the button and line up vertically
    #   3. Push the button
    # We need to first move the robot to the side of the wall to get a clear
    # line of sight to the button.
    if check("the robot is not positioned to the side of the wall"):
        robot.move("to the side of the wall")
    # Once we're positioned to the side of the wall, we can move the gripper in
    # front of the button and line it up vertically.
    if check("the robot's gripper is not in front of the button"):
        robot.move_gripper("in front of the button")
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up with the button, we can push it.
    if check("the robot's gripper is vertically aligned with the button"):
        robot.move_gripper("near the button")