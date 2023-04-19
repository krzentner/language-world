# disassemble: pull the wrench off the peg
# def disassemble(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Lift the wrench up and out of its socket
    #  4. Move the wrench to a different location
    # First, place the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # Now that the gripper is above the wrench, grab it with the gripper.
    if check("the robot's gripper is vertically aligned with the wrench and the robot's gripper is not around the wrench"):
        robot.move_gripper("around the wrench", close_gripper=True)
    # With the wrench in the gripper, lift it out of its socket.
    if check("the wrench is in the robot's gripper and the gripper is not in a raised position"):
        robot.move_gripper("above the peg")
    # Move the wrench to a different location for disassembly.
    if check("the robot's gripper is above the desired location"):
        robot.move_gripper("near the desired location")