# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Put gripper around the peg
    #  4. Release wrench to wrap it around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench becomes left of the gripper, go back to putting the gripper
    # above the wrench.
    # Check if the gripper is lined up with the wrench from the front instead of
    # around it, since the wrench is long and thin.
    if check("wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.grab("wrench")
    # If the wrench is grabbed, put the gripper around the peg.
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the gripper is lined up with the peg, put it around the peg.
    if check("the robot's gripper is horizontally aligned with the peg"):
        robot.put("gripper around peg")
    # Release the wrench to wrap it around the peg.
    if check("the wrench is wrapped around the peg"):
        robot.release("wrench")