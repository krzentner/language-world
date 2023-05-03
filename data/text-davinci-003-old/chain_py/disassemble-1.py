
    # Steps:
    #  1. Line up the robot's gripper with the peg as seen from the top
    #  2. Pull the wrench off the peg
    # First, move the robot's gripper to the correct position.
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    # Move the robot's gripper downward to surround the peg.
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around the peg"):
        robot.grab("peg")
    # Now that the peg is enclosed by the gripper, start pulling it off the peg.
    if check("the robot's gripper is around the peg"):
        robot.pull("wrench off peg")