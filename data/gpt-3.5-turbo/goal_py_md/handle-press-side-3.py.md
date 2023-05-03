# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Position gripper next to handle
    #  2. Push down on handle from side
    # Put the gripper near the handle
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # Once gripper is near the handle, push down on the handle
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("on top of the handle", close_gripper=True)
        robot.move_gripper("next to the handle")