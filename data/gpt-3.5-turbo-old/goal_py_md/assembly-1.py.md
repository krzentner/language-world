# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    #   1. Put gripper above the wrench
    #   2. Grab the wrench with the gripper
    #   3. Move gripper to be above the peg
    #   4. Release the wrench to let it fall onto the peg
    #   5. Close the gripper to ensure the wrench is tightly around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the gripper isn't around the wrench, put it around the wrench.
    if check("the robot's gripper is not around the wrench and the robot's gripper is open"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # If the gripper is around the wrench, move it above the peg.
    if check("the robot's gripper is around the wrench"):
        robot.move_gripper("above the peg")
    # If the gripper is above the peg, release the wrench to let it fall onto
    # the peg.
    if check("the robot's gripper is above the peg and the wrench is not around the peg"):
        robot.release_gripper()
    # If the wrench is around the peg, close the gripper to ensure the wrench is
    # tightly around the peg.
    if check("the wrench is around the peg and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)