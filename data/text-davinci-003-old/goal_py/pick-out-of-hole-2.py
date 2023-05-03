
    # Steps:
    #  1. Put gripper at the top of the peg
    #  2. Pull up on the peg with the gripper
    #  3. Move the peg to the target location
    # First, the robot needs to put the gripper above the peg, so that it can
    # grab the top of it in the next step.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # If the robot's gripper is not near the peg or aligned with the peg, move
    # it near the peg.
    if check("the robot's gripper is near the peg and the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", close_gripper=True)
    # Once the gripper is lined up with the peg, start to pull up on the peg.
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is closed"):
        robot.move_gripper("above the peg")
    # Once the peg is out of the hole, move it to the target location.
    if check("the robot's gripper is above the peg"):
        robot.move_gripper("near the target location")