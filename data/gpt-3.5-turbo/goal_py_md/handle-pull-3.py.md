# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Open gripper around handle
    #  3. Close gripper around handle
    #  4. Lift up the handle
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.move_gripper("near the handle", close_gripper=True)
    if check("the robot's gripper is around handle and the handle is down"):
        robot.move_gripper("up and slightly backward of the handle")