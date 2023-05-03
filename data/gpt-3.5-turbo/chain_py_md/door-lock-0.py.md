# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper around dial
    #  2. Turn dial to lock position
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.drop("gripper around dial")
    # Turn the dial to the lock position by rotating it clockwise.
    if check("the robot's gripper is around the dial"):
        robot.rotate("dial clockwise to lock position")