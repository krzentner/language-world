

# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Wrap the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the gripper isn't around or near the wrench, move the gripper around the wrench.
    if check("the robot's gripper is not around or near the wrench"):
        robot.grab("wrench")
    # If the wrench is near the gripper, we can start to wrap it around the peg.
    if check("the wrench is near the gripper"):
        robot.wrap("wrench around peg")