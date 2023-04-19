# disassemble: pull the wrench off the peg
# def disassemble(robot):
    # Steps:
    # 1. Put gripper above the wrench
    # 2. Grab the wrench with the gripper
    # 3. Pull the wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the gripper isn't around the wrench, put it around the wrench.
    if check("the robot's gripper is not around the wrench and the robot's gripper is open"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # If the gripper is near the wrench and already holding it, pull the wrench
    # off the peg.
    # We can do this by lifting the wrench up vertically and then pulling it back.
    if check("the robot's gripper is near the wrench and the wrench is not lifted up"):
        robot.move_gripper("above the wrench")
    if check("the robot's gripper is above the wrench and the wrench is still attached to the peg"):
        robot.move_gripper("away from the peg")