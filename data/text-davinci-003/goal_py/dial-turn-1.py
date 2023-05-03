
    # Steps:
    #  1. Orient the gripper as viewed from in front
    #  2. Push down on the dial and turn it
    # We need to line the gripper up with the dial as seen from in front.
    # If the grip isn't lined up as seen from in front, move the grip to that
    # angle.
    if check("the robot's gripper is not forward aligned with the dial"):
        robot.move_gripper("forward aligned with the dial", close_gripper=True)
    # If the grip isn't far away from the dial, move it closer.
    if check("the robot's gripper is forward aligned with the dial and the robot's gripper is not close to dial"):
        robot.move_gripper("close to the dial")
    # If the gripper is close to the dial, we can turn it.
    if check("the robot's gripper is close to dial"):
        robot.move_gripper("above the dial")