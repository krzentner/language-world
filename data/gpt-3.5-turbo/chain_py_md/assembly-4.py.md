# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put gripper above wrench
    #  2. Grab wrench with gripper
    #  3. Put gripper above peg
    #  4. Drop wrench around peg and close gripper
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench becomes left of the gripper, go back to putting the gripper
    # above the wrench.
    # Because the wrench is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.grab("wrench")
    # Once we have the wrench, we can put the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # If the gripper isn't around the peg, put the gripper around the peg.
    # We'll wrap the wrench around the peg at the same time we drop it around the
    # peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper and wrench around peg")