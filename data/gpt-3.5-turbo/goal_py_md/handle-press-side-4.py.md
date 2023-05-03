# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put the gripper to the left of the handle
    #  2. Push down on the handle from the side
    # Position the gripper to the left of the handle.
    if check("the robot's gripper is not left of the handle"):
        robot.move_gripper("left of the handle", close_gripper=True)
    # Once the gripper is positioned to the left of the handle, push down on the handle.
    if check("the robot's gripper is left of the handle"):
        robot.move_gripper("below the handle")