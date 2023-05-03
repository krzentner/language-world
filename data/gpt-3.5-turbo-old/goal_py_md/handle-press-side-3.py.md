# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper to the right of the handle
    #  2. Move gripper down and push the handle down
    #  3. Push the handle further down
    # First, move the robot's gripper to the right of the handle.
    if check("the robot's gripper is not aligned with the handle"):
        robot.move_gripper("right of the handle")
    # Next, move the gripper down and push the handle down.
    if check("the robot's gripper is not below the handle"):
        robot.move_gripper("below the handle", close_gripper=True)
    # If the gripper is below the handle and the handle isn't pushed down all
    # the way, push it down some more.
    if check("the robot's gripper is below the handle and the handle is not fully pushed down"):
        robot.move_gripper("fully pushed down")