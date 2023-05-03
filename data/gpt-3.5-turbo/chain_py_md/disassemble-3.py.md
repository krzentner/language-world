# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Move the wrench to the side
    #  4. Pull the wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench isn't inside the gripper, grab it with the gripper.
    if check("the wrench is not inside the gripper"):
        robot.grab("wrench")
    # Move the wrench to the side so that it doesn't hit the peg when we pull it off.
    if check("the wrench is not to the side of the peg"):
        robot.move("wrench to the side of the peg")
    # Pull the wrench off the peg.
    if check("the wrench is on the peg and the gripper is not pulling the wrench off"):
        robot.pull("wrench off the peg")