

# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    #  1. Put gripper wrench above the peg
    #  2. Drop gripper around the wrench
    #  3. Close gripper around the wrench
    #  4. Move wrench around the peg

    # First, put the gripper above the wrench so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the gripper isn't around the wrench, put it around the wrench.
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.move_gripper("around the wrench", close_gripper=True)
    # If the gripper is near the wrench and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is above wrench and the robot's gripper is closed"):
        robot.move_gripper("above the peg")
    # Once the wrench is grabbed, rotate it to place it around the peg.
    if check(robot's gripper is around the wrench):
        robot.move_gripper("around the peg", rotate_gripper=True)