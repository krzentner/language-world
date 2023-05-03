# Steps:
    #  1. Put gripper above hole
    #  2. Drop gripper into hole until it hits peg
    #  3. Grip the peg
    #  4. Pull the gripper and peg out of the hole
    #  5. Move peg to goal
    # First, put the gripper roughly above the hole, so that we can see where the
    # peg is and avoid hitting the sides of the hole.
    if check("the robot's gripper is not above hole"):
        robot.place("gripper above hole")
    # Move the gripper down into the hole until it hits the peg.
    if check("the robot's gripper is not around peg"):
        robot.put("gripper into hole until it touches peg")
    # Grip the peg if the gripper is around it.
    if check("the robot's gripper is around peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # If the gripper is around the peg and closed, pull the gripper and the peg
    # out of the hole.
    if check("the robot's gripper is around peg and the robot's gripper is closed and the gripper is inside the hole"):
        robot.pull("gripper and peg out of the hole")
    # If the gripper and peg are out of the hole, move the peg to the goal
    # location.
    if check("the robot's gripper is holding the peg and is at the goal location"):
        robot.place("peg at goal")