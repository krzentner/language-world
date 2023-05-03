# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Move gripper to the door dial
    #  2. Turn the dial to the correct combination
    #  3. Pull the handle to unlock the door
    # Move the gripper to the door dial.
    if check("the robot's gripper is not near the door dial"):
        robot.move_gripper("near the door dial")
    # Turn the dial to the correct combination.
    if check("the dial is not set to the correct combination"):
        robot.turn_dial("to the correct combination")
    # Pull the handle to unlock the door.
    if check("the dial is set to the correct combination and the robot's gripper is near the door handle"):
        robot.move_gripper("around the door handle")