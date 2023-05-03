
    # Steps:
    #  1. Move gripper to dial
    #  2. Rotate dial
    #  3. Line up with the target number
    # Move the robot's gripper to the dial.
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper to dial")
    # Once the gripper is near the dial, rotate it.
    # We just need to be enough in position to be able to then line it up with the
    # target number.
    if check("the robot's gripper is near the dial and the dial is not rotated to target"):
        robot.rotate("dial")
    # Line up the dial with the target number.
    if check("the robot's gripper is near the dial and the dial is not aligned with target"):
        robot.align("dial to target")