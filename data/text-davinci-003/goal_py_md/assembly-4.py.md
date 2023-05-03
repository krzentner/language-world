

# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put gripper above wrench
    #  2. Drop gripper around wrench handle
    #  3. Close gripper around wrench handle
    #  4. Line up wrench with peg
    #  5. Wrap the wrench around the peg
    # First, move the gripper above the wrench.
    if check("the robot's gripper is not above wrench handle"):
        robot.move_gripper("above the wrench handle")
    # Then, put the gripper around the handle.
    if check("the robot's gripper is not around wrench handle and the robot's gripper is open"):
        robot.move_gripper("near the wrench handle", close_gripper=True)
    # Once the wrench is lined up, move it to the peg.
    if check("the robot's gripper is forward aligned with the wrench handle and the robot's gripper is closed"):
        robot.move_gripper("near the peg")
    # Now, line the wrench up with the peg.
    if check("the robot's gripper is near peg and the wrench is not horizontally aligned with peg"):
        robot.move_gripper("horizontally aligned with peg")
    # Finally, move the gripper above the peg and then wrap the wrench around
    # the peg.
    if check("the robot's gripper is horizontally aligned with peg"):
        robot.move_gripper("above the peg")
        robot.move_gripper("around the peg")