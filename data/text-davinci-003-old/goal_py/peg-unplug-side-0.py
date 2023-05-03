
    # Steps:
    #  1. Put gripper near peg
    #  2. Grab peg
    #  3. Pull peg out to the side
    # First, line the gripper up with the peg from the front.
    if check("the robot's gripper is not forward aligned with the peg"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # Now we should be able to unplug the peg by pulling it to the side.
    if check("the robot's gripper is forward aligned with the peg"):
        robot.move_gripper("left of the peg")