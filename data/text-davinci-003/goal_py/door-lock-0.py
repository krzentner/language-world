
    # Steps:
    #  1. Put gripper below the door lock's dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial in the direction to lock the door
    # Put the gripper as close to directly below the door lock's dial as
    # possible.
    if check("the robot's gripper is not above door lock's dial"):
        robot.move_gripper("below the door lock's dial")
    # If the gripper is not near the door lock's dial, move it to the door lock's
    # dial.
    if check("the robot's gripper is above the door lock's dial and the robot's gripper is not near the door lock's dial"):
        robot.move_gripper("near the door lock's dial")
    # If the gripper is near the door lock's dial, grab it and turn in the
    # correct direction (clockwise to lock the door).
    if check("the robot's gripper is near the door lock's dial"):
        robot.move_gripper("clockwise")