# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    # 1. Put gripper above the wrench
    # 2. Grab the wrench with the gripper
    # 3. Put gripper above the peg
    # 4. Align the wrench with the peg
    # 5. Move gripper around the peg to put wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the wrench isn't around the gripper, put it around the wrench.
    if check("the robot's gripper is not around the wrench and the robot's gripper is open"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # Move the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # Align the wrench around the peg.
    if check("the robot's gripper is forward aligned with the peg and the wrench is not horizontally aligned with the peg"):
        robot.move_gripper("horizontally aligned with the peg")
    # Move the gripper around the peg to put wrench around the peg.
    if check("the robot's gripper is horizontally aligned with the peg and the wrench is around the peg and the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", close_gripper=True)