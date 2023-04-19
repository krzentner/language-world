# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    # 1. Put gripper right of the handle
    # 2. Move gripper down around the handle
    # 3. Close the gripper around the handle
    # 4. Lift up the handle
    # First, align the gripper with the handle from the side
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the gripper is aligned with the handle but isn't around it yet, move it
    # down and close around the handle
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    # If the gripper is around the handle, lift it up
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle", close_gripper=True)