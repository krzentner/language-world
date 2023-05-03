# Steps:
#   1. Put gripper near the door handle
#   2. Turn the dial in the correct direction
#   3. Turn the dial until the lock clicks open
# First, put the gripper near the door handle.
if check("the robot's gripper is not near the door handle"):
    robot.move("gripper near the door handle")
# Determine which way to turn the dial based on the current position and the
# desired position of the lock.
if check("the dial is not turned towards the unlock position"):
    if check("the dial is turned to the right of the unlock position"):
        robot.turn("the dial left")
    else:
        robot.turn("the dial right")
# Keep turning the dial until the lock clicks open.
while check("the lock is not unlocked"):
    robot.turn("the dial left")