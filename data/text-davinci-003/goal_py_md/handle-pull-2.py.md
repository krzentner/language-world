

# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab handle with the gripper
    #  3. Pull the handle up
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # Once the gripper is lined up above the handle, we should be able to grab
    # the handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.move_gripper("around the handle")
    # Once the gripper is around the handle, we can just pull the handle up.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("upward and away from the handle")