# door-unlock: turn the dial on the door
# def door_unlock(robot):
    # Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial until the lock opens
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the door dial and the robot's gripper is open"):
        robot.move_gripper("around the door dial", close_gripper=True)
    # Now that the gripper is around the dial, turn the dial until the lock opens.
    # We can turn the dial by rotating the gripper clockwise.
    if check("the robot's gripper is around the door dial"):
        robot.rotate_gripper(clockwise=True, speed=1)
        if check("the lock has opened"):
            robot.stop_gripper_rotation()