

# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Move the robot's gripper to the wrench
    #  2. Grab the wrench with the robot's gripper
    #  3. Line up the wrench with the peg
    #  4. Rotate the wrench around the peg
    # First, move the robot's gripper to the wrench.
    if check("the robot's gripper is not near the wrench"):
        robot.move_gripper("near the wrench")
    # Next, if the wrench is still above the gripper, grab it with the gripper.
    if check("the robot's gripper is not around the wrench"):
        robot.move_gripper("above the wrench", close_gripper=True)
    # Once the gripper has the wrench, line the wrench up with the peg.
    if check("the robot's gripper is around the wrench and the wrench is not horizontally aligned with the peg"):
        robot.move_gripper("horizontally aligned with the peg")
    # When the wrench is in place, rotate the wrench around the peg to secure it.
    if check("the robot's gripper is around the wrench and the wrench is horizontally aligned with the peg"):
        robot.move_gripper("above the peg")