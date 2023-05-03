

Below it, write code to explain how the robot should perform the task of pushing a handle down.

# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the handle from the top
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is not near the handle and the robot's gripper is vertically aligned with the handle"):
        robot.move_gripper("near the handle")