# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put gripper near the handle
    #  2. Push down on the handle
    # First, move the gripper near the handle. For this task, we don't need to be
    # too precise in our alignment.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # Once the gripper is near the handle, just push down on it.
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("down on the handle")