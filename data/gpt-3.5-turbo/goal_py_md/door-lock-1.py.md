# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put the gripper above the dial
    #  2. Drop the gripper around the dial
    #  3. Turn the dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not almost vertically aligned with the dial"):
        robot.move_gripper("almost vertically aligned with the dial", close_gripper=True)
    # Once the gripper is mostly vertically aligned with the dial, drop the gripper around the dial.
    if check("the robot's gripper is almost vertically aligned with the dial and the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Turn the dial to unlock the door.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("turned dial")