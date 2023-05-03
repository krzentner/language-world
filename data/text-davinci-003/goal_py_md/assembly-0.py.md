

# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put the gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Line up the wrench with the peg
    #  4. Slide the wrench around the peg
    # Put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # Next, grab the wrench with the gripper.
    if check("the robot's gripper is not around wrench"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # If the gripper is around the wrench, line up the wrench with the peg.
    # The peg should be directly left of the wrench as seen from the front.
    if check("the peg is not left of the wrench and the peg is not forward aligned with the wrench"):
        robot.move_gripper("left of the peg")
    # Once the wrench is lined up with the peg, we can slide the wrench around
    # the peg.
    if check("the peg is left of the wrench and the peg is forward aligned with the wrench"):
        robot.move_gripper("horizontally aligned with hole")