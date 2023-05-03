# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Push down on the handle
    if check("the robot's gripper is not above handle"):
        robot.move_gripper("above the handle")
    # Once the gripper is lined up above the handle, just push down on it.
    if check("the robot's gripper is above handle"):
        robot.move_gripper("near the handle")