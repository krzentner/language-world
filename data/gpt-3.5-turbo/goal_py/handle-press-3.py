# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Line up the gripper horizontally with the handle
    #  2. Push down on the handle
    # We need to line up the gripper horizontally with the handle.
    if check("the gripper is not horizontally aligned with the handle"):
        robot.move_gripper("horizontally aligned with the handle", close_gripper=True)
    # Once the gripper is in position, we can push down on the handle.
    if check("the gripper is horizontally aligned and near the handle"):
        robot.move_gripper("above the target location")