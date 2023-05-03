# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Put gripper above the peg
    #  4. Wrap the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench becomes left of the gripper, go back to putting the gripper
    # above the wrench.
    # Because the wrench is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.grab("wrench")
    # Put the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # If the gripper is above the peg, wrap the wrench around it.
    if check("the robot's gripper is above the peg"):
        robot.wrap("wrench around the peg")