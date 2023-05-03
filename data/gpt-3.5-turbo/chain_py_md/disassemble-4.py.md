# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    # 1. Put gripper above the wrench
    # 2. Grab the wrench
    # 3. Lift the wrench off the peg
    # 4. Move the wrench away from the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench is not in the gripper, grab it.
    if check("the wrench is not in the robot's gripper"):
        robot.grab("wrench")
    # Once the wrench is in the gripper, lift it off the peg.
    if check("the wrench is in the robot's gripper and the robot's gripper is touching the peg"):
        robot.pull("the wrench off the peg")
    # Finally, move the wrench away from the peg.
    if check("the wrench is in the robot's gripper and the robot's gripper is not near the goal"):
        robot.move("gripper away from the peg")