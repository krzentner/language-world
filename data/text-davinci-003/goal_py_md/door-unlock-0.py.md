

# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Put gripper in dial
    #  2. Turn the dial to the correct number
    # Put the robot's gripper into the dial.
    if check("the robot's gripper is not in the dial"):
        robot.move_gripper("into the dial", close_gripper=True)
    # Turn the dial to the correct number.
    if check("the robot's gripper is in the dial"):
        robot.move_gripper("to the correct number")