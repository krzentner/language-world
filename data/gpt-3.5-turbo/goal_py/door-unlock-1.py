# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Put gripper near the dial
    #  2. Turn the dial
    # If the gripper is not near the dial, move it there.
    if check("the robot's gripper is not near the dial"):
        robot.move_gripper("near the dial")
    # Turn the dial clockwise to unlock the door.
    robot.turn_gripper(30) # turn gripper 30 degrees
    robot.turn_gripper(30) # turn gripper another 30 degrees
    robot.turn_gripper(30) # turn gripper another 30 degrees
    robot.turn_gripper(30) # turn gripper another 30 degrees
    robot.turn_gripper(30) # turn gripper another 30 degrees
    robot.turn_gripper(30) # turn gripper another 30 degrees
    robot.turn_gripper(10) # turn gripper a final 10 degrees to complete the rotation.