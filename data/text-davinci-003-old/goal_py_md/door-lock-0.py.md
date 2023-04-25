

Steps:
1. Put gripper near the door handle
2. Put gripper above the dial
3. Turn the dial

# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put gripper near the door handle
    #  2. Put gripper above the dial
    #  3. Turn the dial
    # Put the gripper near the door handle to start.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the gripper isn't above the dial, move it above the dial.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial", close_gripper=True)
    # If the gripper is above the dial, start turning it.
    if check("the robot's gripper is above the dial"):
        robot.move_gripper("clockwise around the dial")