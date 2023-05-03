# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Move gripper to the dial
    #  2. Grab and hold the dial
    #  3. Turn the dial to the desired combination
    #  4. Release the dial
    # First, move the gripper to the dial.
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper to the dial")
    # Once the gripper is near the dial, grab and hold the dial.
    if check("the robot's gripper is near the dial and the robot's gripper is open"):
        robot.hold("dial")
    # Now that the gripper is holding the dial, turn it to the desired combination.
    if check("the robot's gripper is holding the dial"):
        robot.turn("the dial to the desired combination")
    # Finally, release the dial.
    if check("the dial is at the desired combination and the robot's gripper is holding the dial"):
        robot.release("dial")