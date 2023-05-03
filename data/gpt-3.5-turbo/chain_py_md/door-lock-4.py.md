# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial clockwise to lock
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the door lock dial"):
        robot.drop("gripper around the dial")
    # Once the gripper is around the dial, turn the dial clockwise to lock it.
    if check("the robot's gripper is around the dial and the dial is not locked"):
        robot.turn("dial clockwise")