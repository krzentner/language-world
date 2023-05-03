
    # Steps:
    #  1. Put gripper left of the peg
    #  2. Push down on peg to grip it
    #  3. Move peg left to align it with hole
    #  4. Push peg into hole
    # We need to push the peg down to grip it, so first move the gripper
    # parallel to the peg left.
    if check("the robot's gripper is not left of the peg"):
        robot.move_gripper("left of the peg")
    # Now move down and push the peg, so that the peg is in the gripper.
    if check("the robot's gripper is left of the peg and the robot's gripper is not below the peg"):
        robot.move_gripper("below the peg", close_gripper=True)
    # Move the peg left to align with the hole.
    if check("the robot's gripper is below the peg and the peg is aligned with the hole from the side"):
        robot.move_gripper("left of the target location")
    # Push the peg into the hole.
    if check("the robot's gripper is left of the target location"):
        robot.move_gripper("in front of the target location")