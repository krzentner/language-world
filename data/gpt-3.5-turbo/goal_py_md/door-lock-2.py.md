# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Drop gripper around the dial
    #  3. Turn the dial right until locked
    # First, put the gripper mostly above the dial, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not almost vertically aligned with the dial"):
        robot.move_gripper("almost vertically aligned with the dial", close_gripper=True)
    # Once the gripper is around the dial, turn it right until it's locked.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("horizontally aligned with the dial", close_gripper=True)
        while True:
            if check("the dial is not locked"):
                robot.rotate_gripper("clockwise")
            else:
                break