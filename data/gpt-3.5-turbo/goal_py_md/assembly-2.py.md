# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put the gripper above the wrench
    #  2. Close the gripper around the wrench
    #  3. Line up the wrench with the peg
    #  4. Wrap the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the gripper isn't around the wrench, put it around the wrench.
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # If the gripper is near the wrench and closed, move the wrench to the top of the peg.
    if check("the robot's gripper is near the wrench and the robot's gripper is closed and the wrench is not above the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper is above the peg and the wrench is not wrapped around the peg, wrap the wrench around the peg.
    if check("the robot's gripper is above the peg and the wrench is not wrapped around the peg"):
        robot.move_gripper("around the peg")