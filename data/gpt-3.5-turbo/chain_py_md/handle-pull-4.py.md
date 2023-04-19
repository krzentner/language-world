# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    # 1. Put the gripper around the handle
    # 2. Pull up the handle
    # Put the gripper around the handle.
    if check("the robot's gripper is not around handle"):
        robot.grab("the handle")
    # Pull up the handle.
    if check("the handle is not up"):
        robot.pull("the handle up")