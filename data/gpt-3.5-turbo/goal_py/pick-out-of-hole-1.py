# Steps:
    #  1. Put gripper above the peg in the hole
    #  2. Grab the peg with the gripper
    #  3. Lift the peg out of the hole
    #  4. Move the peg to the target location
    # First, put the gripper above the peg in the hole.
    if check("the robot's gripper is not vertically aligned with the peg in the hole"):
        robot.move_gripper("vertically aligned with the peg in the hole")
    # If the gripper is not around the peg, grab it.
    if check("the robot's gripper is not around the peg in the hole and the robot's gripper is open"):
        robot.move_gripper("above the peg in the hole", close_gripper=True)
    # Once the gripper is around the peg, lift it out of the hole.
    if check("the robot's gripper is around the peg in the hole"):
        robot.move_gripper("above the target location")