
    # Steps:
    #  1. Put gripper above lever
    #  2. Rotate lever upward
    # To start turning the lever, we need to align the gripper with the lever
    # when viewed from above.
    if check("the robot's gripper is not almost vertically aligned with lever"):
        robot.move_gripper("almost vertically aligned with the lever", close_gripper=True)
    # Once the gripper is lined up with the lever, we can start rotating it
    # upward.
    if check("the robot's gripper is vertically aligned with lever"):
        robot.move_gripper("right of the lever")

# valve-turn-left: turn the valve left
# def valve_turn_left(robot):
    # Steps:
    #  1. Put gripper in front of valve
    #  2. Start turning the valve left
    # We can start turning the valve by positioning the gripper roughly in front
    # of it.
    if check("the robot's gripper is not forward aligned with the valve"):
        robot.move_gripper("forward aligned with the valve", close_gripper=True)
    # Once the gripper is facing the valve we can start turning it left
    if check("the robot's gripper is forward aligned with the valve"):
        robot.move_gripper("left of the valve")