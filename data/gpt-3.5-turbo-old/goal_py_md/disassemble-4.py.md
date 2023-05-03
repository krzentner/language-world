# disassemble: pull the wrench off the peg
# def disassemble(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Move the wrench away from the peg
    #  4. Release the wrench
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the gripper is not around the wrench, grab the wrench with the gripper.
    if check("the robot's gripper is not around the wrench and the robot's gripper is not holding the wrench"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # Once the gripper is around the wrench, we can move the wrench away from the peg horizontally.
    if check("the robot's gripper is holding the wrench and the wrench is not horizontally aligned with the robot's gripper"):
        robot.move_gripper("left of the peg holding the wrench")
    # Once the wrench is away from the peg, we can release it.
    if check("the wrench is horizontally aligned with the robot's gripper and the robot's gripper is not open"):
        robot.move_gripper("vertically aligned with the peg holding the wrench", close_gripper=False)