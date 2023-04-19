
    # Steps:
    #  1. Put gripper horizontally above the wrench
    #  2. move gripper down along the wrench
    #  3. Pull wrench off the peg
    # First, put the gripper horizontally above the wrench.
    if check("the robot's gripper is not horizontally aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the gripper is not near the wrench and the wrench is fully in view,
    # the gripper should be moved downward along the wrench.
    if check("the robot's gripper is not near wrench and wrench is fully visible"):
        robot.move("gripper down along wrench")
    # If the robot's gripper is near the wrench, pull it off.
    if check("the robot's gripper is near wrench"):
        robot.pull("wrench off peg")