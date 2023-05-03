
    # Steps:
    #  1. Put gripper above peg
    #  2. Grab the wrench with the gripper
    #  3. Pull away from the peg
    # First, put the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # As long as the gripper is lined up with the wrench and doesn't have it yet,
    # grab the wrench.
    if check("the robot's gripper is forward aligned with wrench and the robot's gripper is not around wrench"): 
        robot.grab("wrench")
    # Once we have the wrench in our gripper, pull away from the peg.
    if check("the robot's gripper is around wrench and wrench is still part of peg"):
        robot.pull("away from peg")