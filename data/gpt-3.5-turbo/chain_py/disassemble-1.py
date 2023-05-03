# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    #  1. Put the gripper above the wrench
    #  2. Open the gripper and grab the wrench by the handle
    #  3. Pull the wrench off the peg
    # First, put the gripper above the wrench so that we can grasp it easily.
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    # If the gripper is above the wrench, we can open it and grab the wrench by
    # the handle.
    if check("the robot's gripper is above the wrench and the robot's gripper is open"):
        robot.grab("wrench by handle")
    # Once we have the wrench, we can pull it off the peg.
    if check("the robot's gripper is holding the wrench and the wrench is attached to the peg"):
        robot.pull("wrench off the peg")