
    # Steps:
    #  1. Line up gripper above hole
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Lift peg out of hole
    # First, we need to get the gripper above the hole, so it can drop down and
    # trap the peg.
    if check("the robot's gripper is not above hole"):
        robot.put("gripper above hole")
    # Once the gripper is roughly above the hole, it should drop around the peg if the 
    # peg is there.
    if check("the robot's gripper is above hole and the robot's gripper is open"):
        robot.drop("gripper around peg")
    # If the gripper is already around the peg, it can just close around the peg.
    if check("the robot's gripper is around peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # Once the gripper is closed, we can lift the peg out of the hole.
    if check("the robot's gripper is closed and the peg is cleared from the hole"):
        robot.lift("peg from hole")