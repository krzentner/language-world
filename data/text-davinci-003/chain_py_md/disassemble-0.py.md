

# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Pull the wrench off the peg
    # First, put the gripper above the wrench. We don't know the exact location
    # of the wrench, so just get it near the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    # If the wrench is left of the center of the robot's gripper, grab it.
    # This assumes the robot's gripper is closed; if the robot's gripper is
    # open it will need to close it first.
    if check("the wrench is left of the center of the robot's gripper and the robot's gripper is closed"):
        robot.grab("wrench")
    # If the wrench is near the robot's gripper, start pulling it off the peg.
    # We don't need to be precise about how much the robot pulls so it can just
    # be a small movement.
    if check("the wrench is near the robot's gripper"):
        robot.pull("the wrench off the peg")