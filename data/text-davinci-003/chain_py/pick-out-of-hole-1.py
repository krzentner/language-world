
    # Steps:
    #  1. Move gripper above hole
    #  2. Drop gripper into hole around peg
    #  3. Close gripper around peg
    #  4. Pull peg out of hole
    #  5. Move peg to target location
    # First, move the gripper above the hole.
    if check("the robot's gripper is not above hole"):
        robot.move("gripper above hole")
    # If the gripper is not around the peg, drop the gripper around the peg.
    if check("the robot's gripper is not around peg"):
        robot.drop("gripper into hole")
    # Close the gripper to try to grab the peg.
    if check("the robot's gripper is around peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # If the gripper is closed around the peg, pull the peg out of the hole
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.pull("peg out of hole")
    # If the peg is not connected to the gripper, move the peg to the goal.
    if check("peg is not connected to the robot's gripper"):
        robot.place("peg at goal")