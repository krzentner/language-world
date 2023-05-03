# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Position the gripper around the dial
    #  2. Turn the dial to the correct position
    # If the gripper is not near the dial, move it there.
    if check("the robot's gripper is not near the door lock dial"):
        robot.grab("door lock dial")
    # If dial is not at the correct position, turn it to the correct position.
    if check("the lock is not secured"):
        robot.turn("dial to secure lock")