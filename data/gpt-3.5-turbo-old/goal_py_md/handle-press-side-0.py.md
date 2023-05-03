# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper near the handle
    #  2. Push down on the handle from the side
    # First, put the gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # If the gripper is near the handle, push down on it from the side.
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("sideways aligned with the handle", close_gripper=True)