# disassemble: pull the wrench off the peg
# def disassemble(robot):
    # Steps:
    #  1. Put gripper above wrench
    #  2. Grab the wrench with the gripper
    #  3. Move the gripper away from the peg
    #  4. Release the wrench
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench is not in the gripper, we can grab it.
    if check("the wrench is not in the robot's gripper"):
        robot.grab("the wrench")
    # Now, move the gripper away from the peg.
    if check("the robot's gripper is near the peg"):
        robot.move("gripper away from the peg")
    # Finally, release the wrench.
    if check("the robot's gripper is away from the peg"):
        robot.release("the wrench")