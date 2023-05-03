# Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around peg
    #  3. Grab the peg
    #  4. Pull the peg out of the hole
    #  5. Move the peg to the target location
    # First, position the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper is not around the peg, move it around the peg and close
    # the gripper.
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is around the peg, pull the peg out of the hole.
    if check("the robot's gripper is around the peg and the peg is in the hole"):
        robot.move_gripper("horizontally aligned with the peg")
    # Move the gripper with the peg from the hole to the target location.
    if check("the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")