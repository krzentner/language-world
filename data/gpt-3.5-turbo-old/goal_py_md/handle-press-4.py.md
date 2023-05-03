# handle-press: push down the handle
# def handle_press(robot):
    # Steps:
    #  1. Move gripper above the handle
    #  2. Drop gripper around the handle
    #  3. Press the handle down
    # Begin by moving the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # If the gripper is not around the handle, position it so it can grasp the handle.
    if check("the robot's gripper is not around the handle and the robot's gripper is open"):
        robot.move_gripper("near the handle", close_gripper=True)
    # If the gripper is not pressing down on the handle, move it down to activate the handle.
    if check("the robot's gripper is around the handle and the handle is not pressed down"):
        robot.move_gripper("near the top of the handle")