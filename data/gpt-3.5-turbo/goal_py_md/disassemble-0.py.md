# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    # 1. Put gripper above the wrench
    # 2. Grab the wrench with the gripper
    # 3. Move the wrench to the side
    # 4. Release the wrench
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the gripper is above the wrench, grab the wrench.
    if check("the robot's gripper is vertically aligned with the wrench and the robot's gripper is not around the wrench"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # If the wrench is inside the gripper, move it to the side.
    if check("the robot's gripper is around the wrench and the robot's gripper is not horizontally aligned with the peg"):
        robot.move_gripper("right of the peg")
    # Finally, release the wrench.
    if check("the robot's gripper is right of the peg"):
        robot.move_gripper("above the peg", close_gripper=False)