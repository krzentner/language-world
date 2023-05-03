# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Put gripper around dial
    #  2. Turn the dial to the right
    #  3. Stop turning when the dial reaches the correct position
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the door dial"):
        robot.drop("gripper around door dial")
    # Now we can turn the dial by rotating the gripper to the right.
    # Keep turning the gripper until the dial reaches the correct position.
    while check("the dial is not in the correct position"):
        robot.rotate("gripper to the right")
    # If the dial is in the correct position, we're done unlocking the door.