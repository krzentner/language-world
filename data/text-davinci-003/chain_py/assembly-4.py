
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Put the wrench around the peg
    # To grab the wrench and wrap around the peg, start by lining the gripper
    # with the wrench.
    if check("the robot's gripper is not vertically aligned with wrench"):
        robot.put("gripper above wrench")
    # If the wrench is left of the gripper and the gripper is open, grab the
    # wrench and wrap it around.
    if check("the wrench is not left of the gripper and the robot's gripper is open"):
        robot.grab("wrench")
    # If the wrench is right of the gripper and the gripper is closed, we should
    # be able to wrap the wrench around the peg.
    # Try and wrap the wrench around the peg
    if check("the wrench is right of the gripper and the robot's gripper is closed"):
        robot.put("wrench around peg")