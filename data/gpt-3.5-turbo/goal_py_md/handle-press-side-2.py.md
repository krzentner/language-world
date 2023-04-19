# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper to the right of the handle
    #  2. Push down on the handle
    # Put the gripper right of the handle to start pushing it
    if check("the robot's gripper is not right of handle"):
        robot.move_gripper("right of the handle")
    # Push down on the handle to activate it
    if check("the robot's gripper is right of handle"):
        robot.move_gripper("around the handle", close_gripper=True)
        robot.move_gripper("vertically aligned with the handle")
        robot.move_gripper("left of the handle")