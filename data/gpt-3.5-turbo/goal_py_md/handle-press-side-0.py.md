# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper to the left of the handle
    #  2. Push down on the handle from the side
    # If the handle is to the right of the gripper, move the gripper to the left
    # of the handle.
    if check("the handle is not left of the robot's gripper"):
        robot.move_gripper("left of the handle", close_gripper=True)
    # If the gripper is to the left of the handle, push down on the handle.
    if check("the robot's gripper is left of the handle"):
        robot.move_gripper("above the handle")