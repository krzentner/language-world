# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Line up the gripper horizontally with the handle
    #  2. Push down on the handle
    # First, align the gripper horizontally with the handle.
    if check("the robot's gripper is not horizontally aligned with handle"):
        robot.move_gripper("horizontally aligned with the handle", close_gripper=True)
    # Once the gripper is horizontally aligned, just push down on the handle.
    if check("the robot's gripper is horizontally aligned with handle"):
        robot.move_gripper("near the handle")