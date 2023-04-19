

Steps:
1. Put gripper above the dial
2. Drop gripper around the dial
3. Turn the dial

# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Drop gripper around the dial
    #  3. Turn the dial
    # First, put the gripper roughly above the dial, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above dial"):
        robot.move_gripper("above the dial")
    # If the gripper isn't around the dial, put it around the dial.
    if check("the robot's gripper is not around dial and the robot's gripper is open"):
        robot.move_gripper("near the dial", close_gripper=True)
    # If the gripper is near the dial and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above dial and the robot's gripper is closed"):
        robot.move_gripper("around the dial")
    # Once the gripper is around the dial, we can just turn the dial.
    if check("the robot's gripper is around dial"):
        robot.move_gripper("horizontally aligned with the dial")