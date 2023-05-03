# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper near the handle
    #  2. Close gripper around the handle
    #  3. Push down on the handle
    # We need to put the gripper near the handle before we can grab it.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # Once gripper is near the handle, we can grab it by closing the gripper.
    if check("the robot's gripper is near the handle and the gripper is open"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Finally, push down on the handle to press it.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("below the handle")