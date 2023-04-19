# Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the correct position to lock the door
    # If the gripper isn't around the dial, move it there.
    if check("the robot's gripper is not around the dial"):
        robot.put("gripper around the dial")
    # Turn the dial to the correct position to lock the door.
    robot.turn("dial to lock the door")