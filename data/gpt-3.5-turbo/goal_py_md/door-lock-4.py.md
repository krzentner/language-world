# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Move gripper to the dial
    #  2. Turn the dial
    # First, move the gripper close to the dial.
    if check("the robot's gripper is not near the door lock dial"):
        robot.move_gripper("near the door lock dial")
    # Turn the dial to the right to lock the door.
    if check("the robot's gripper is near the door lock dial and the dial is not turned to the right"):
        robot.move_gripper("turn the dial to the right")