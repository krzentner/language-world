
    # Steps:
    #  1. Put the gripper left of the peg
    #  2. Start pulling the peg to the left
    #  3. Grab the peg with the gripper
    #  4. Pull the peg out
    # First, put the gripper left of the peg.
    if check("the robot's gripper is in front of the peg"):
        robot.move_gripper("left of the peg")
    # If the peg is right of the gripper and the gripper isn't close to the peg
    # move the gripper closer.
    if check("the peg is right of the robot's gripper and the robot's gripper is open and the robot's gripper is not near the peg"):
        robot.move_gripper("near peg", close_gripper=True)
    # If the gripper is around the peg, we can try and pull the peg.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("left of peg and slightly above")
    # Once the peg is pulled out, try to line it up with the hole.
    if check("the robot's gripper is left of the peg and the peg is out of the hole"):
        robot.move_gripper("horizontally aligned with hole")