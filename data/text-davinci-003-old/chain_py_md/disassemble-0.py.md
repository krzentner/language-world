

Steps:
1. Put gripper above wrench
2. Drop gripper around wrench
3. Pull wrench off peg

# disassemble: pull the wrench off the peg
# def disassemble(robot):
    # Steps:
    #  1. Put gripper above wrench
    #  2. Drop gripper around wrench
    #  3. Pull wrench off peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench isn't near the gripper, put the gripper around the wrench.
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    # If the gripper is near the wrench, pull the wrench off the peg.
    if check("the robot's gripper is around wrench"):
        robot.pull("wrench off peg")