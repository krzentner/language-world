
    # Steps:
    #  1. Put the robot's gripper above the dial handle
    #  2. Close gripper on the dial handle
    #  3. Turn dial handle to right/left
    # First, put the gripper above the dial handle so that we can grab it.
    if check("the robot's gripper is not almost vertically aligned with the dial handle"):
        robot.move_gripper("almost vertically aligned with the dial handle")
    # Now that the gripper is above the dial handle, we can close it to grab the
    # handle.
    if check("the robot's gripper is vertically aligned with the dial handle"):
        robot.move_gripper("around the dial handle")
    # Once we have grabbed the handle, rotate it counter-clockwise.
    if check("the robot's gripper is above the dial handle"):
        robot.move_gripper("vertically aligned with the dial handle")

# dial-turn-ccw: turn the dial counterclockwise
def dial_turn_ccw(robot):
    # Steps:
    #  1. Put the robot's gripper above the dial handle
    #  2. Close gripper on the dial handle
    #  3. Turn dial handle to right/left
    # First, put the gripper above the dial handle so that we can grab it.
    if check("the robot's gripper is not almost vertically aligned with the dial handle"):
        robot.move_gripper("almost vertically aligned with the dial handle")
    # Now that the gripper is above the dial handle, we can close it to grab the
    # handle.
    if check("the robot's gripper is vertically aligned with the dial handle"):
        robot.move_gripper("around the dial handle")
    # Once we have grabbed the handle, rotate it counter-clockwise.
    if check("the robot's gripper is above the dial handle"):
        robot.move_gripper("vertically aligned with the dial handle")

# dial-turn-cw: turn the dial clockwise
def dial_turn_cw(robot):
    # Steps:
    #  1. Put the robot's gripper above the dial handle
    #  2. Close gripper on the dial handle
    #  3. Turn dial handle to right/left
    # First