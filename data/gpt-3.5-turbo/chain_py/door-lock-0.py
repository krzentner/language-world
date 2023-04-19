# Steps:
    #  1. Move the gripper to the dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial to the correct combination
    # First, move the gripper to the dial we need to turn.
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper to dial")
    # Once the gripper is near the dial, grab it with the gripper.
    if check("the robot's gripper is near the dial and the robot's gripper is not around the dial"):
        robot.grab("dial")
    # Turn the dial to the correct combination by rotating it.
    if check("the robot's gripper is around the dial"):
        robot.rotate("dial to the correct combination")