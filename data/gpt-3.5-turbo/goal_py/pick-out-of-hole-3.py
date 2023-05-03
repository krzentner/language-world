# Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Lift the peg out of the hole
    #  4. Move the peg to the target location
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open and the peg is below the robot's gripper"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is around the peg and the peg is out of the hole, we can
    # move it to the target location.
    if check("the robot's gripper is around peg and the peg is not vertically aligned with hole"):
        robot.move_gripper("near the target location")