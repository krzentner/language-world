# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")
    # If the gripper is not around the dial, grab it with the gripper.
    if check("the robot's gripper is not around dial and the robot's gripper is open"):
        robot.move_gripper("around the dial", close_gripper=True)
    # If the gripper is around the dial, turn it.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("turn the dial")