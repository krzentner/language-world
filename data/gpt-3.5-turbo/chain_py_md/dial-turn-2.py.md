# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the desired position
    # The robot needs to put its gripper around the dial to be able to turn it.
    if check("the robot's gripper is not around the dial"):
        robot.put("gripper around the dial")
    # The robot can turn the dial by rotating its gripper.
    # We can use a while loop to keep rotating the dial until it reaches the
    # desired position.
    desired_position = "position 3" # replace with desired dial position
    while check("the dial is not at the desired position"):
        robot.rotate_gripper("clockwise") # replace with direction to turn the dial
    # Once the dial is at the desired position, the robot can release its
    # gripper from the dial. We could do this by opening the gripper or by
    # moving the gripper away from the dial.