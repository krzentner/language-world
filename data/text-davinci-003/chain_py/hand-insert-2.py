
    # Steps:
    #  1. Put gripper above puck
    #  2. Put gripper around puck
    #  3. Put puck into the hole
    # First, make sure the gripper is above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    # If the gripper is above the puck and still open, grab the puck by closing
    # the gripper.
    if check("the robot's gripper is above the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # If the gripper is closed and still above the puck, try to drop it into the
    # hole.
    if check("the robot's gripper is above the puck and the robot's gripper is closed"):
        robot.drop("puck into hole")