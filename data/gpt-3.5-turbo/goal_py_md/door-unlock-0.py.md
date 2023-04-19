# door-unlock: turn the dial on the door
# def door_unlock(robot):
    # Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial clockwise
    #  3. Turn the dial counterclockwise
    #  4. Turn the dial clockwise
    #  5. Stop turning the dial
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the dial and the robot's gripper is open"):
        robot.move_gripper("around the dial", close_gripper=True)
    # If the gripper is around the dial, turn it clockwise.
    if check("the robot's gripper is around the dial and the robot's gripper is not turned clockwise"):
        robot.move_gripper("turned clockwise")
    # Then turn it counterclockwise.
    if check("the robot's gripper is turned clockwise and the robot's gripper is not turned counterclockwise"):
        robot.move_gripper("turned counterclockwise")
    # Finally, turn it clockwise again.
    if check("the robot's gripper is turned counterclockwise and the robot's gripper is not turned clockwise a second time"):
        robot.move_gripper("turned clockwise")