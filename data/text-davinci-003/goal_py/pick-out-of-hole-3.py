
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Slide peg up out of the hole
    #  5. Move peg to target location
    # First, put the gripper above peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # As long as the peg remains above the gripper, bend the gripper around it.
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around peg"):
        robot.move_gripper("near the peg")
    # If the gripper is around the peg and open, close it to trap the peg.
    if check("the robot's gripper is near peg and the robot's gripper is closed"):
        robot.move_gripper("above the peg")
    # If the gripper is around the peg and closed, we can slide the peg up by
    # moving the gripper up.
    if check("the robot's gripper is above the peg"):
        robot.move_gripper("above the target location")