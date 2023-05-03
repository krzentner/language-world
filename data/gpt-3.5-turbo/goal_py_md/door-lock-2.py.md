# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1.  Put gripper around the dial
    #  2.  Turn the dial clockwise
    # The gripper needs to be around the dial before we can turn it. Align the
    # gripper with the dial.
    if check("the robot's gripper is not around the door handle"):
        robot.move_gripper("around the door handle")
    # If the gripper is around the dial, turn it by rotating clockwise
    if check("the robot's gripper is around the door handle"):
        robot.rotate_gripper("clockwise")