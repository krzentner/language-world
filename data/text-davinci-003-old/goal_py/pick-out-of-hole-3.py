
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around peg
    #  3. Pull peg out of the hole
    #  4. Move peg to target location
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    # If the gripper is near the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.move_gripper("above the peg")
    # Once the peg is in the gripper, pull it out of the hole.
    if check("the robot's gripper is vertically aligned with the peg and the peg is below the robot's gripper"):
        robot.move_gripper("above the target location")