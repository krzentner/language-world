
    # Steps:
    #  1. Put the gripper near the peg
    #  2. Lower the gripper enough to pick the peg up
    #  3. Close the gripper
    #  4. Move the peg to the target location
    #  5. Release the peg at the target location

    # First, put the gripper near the peg.
    if check("the robot's gripper is not near the peg"):
        robot.put("gripper near peg")
    # If the robot's gripper is near the peg but not low enough, lower the
    # gripper so it can grab the peg.
    if check("the robot's gripper is near the peg and the robot's gripper is not low enough to pick up peg"):
        robot.lower("gripper to pick up peg")
    # When the gripper is low enough, close the gripper to grab the peg.
    if check("the robot's gripper is low enough to pick up peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # Now that the gripper is closed and still near the peg, it's probably
    # holding the peg.
    # Move the peg to the target location.
    if check("the robot's gripper is near peg and the robot's gripper is closed"):
        robot.move("peg to goal")
    # When the peg is at the target location, open the gripper to
    # release the peg.
    if check("the peg is at the goal"):
        robot.open("gripper around peg")