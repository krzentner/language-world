# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper next to the handle
    #  2. Push down on the handle
    if check("the robot's gripper is not next to the handle"):
        robot.move_gripper("next to the handle", close_gripper=True)
    if check("the robot's gripper is next to the handle"):
        robot.move_gripper("near the handle")