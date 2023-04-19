
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper down the hole
    #  3. Push peg up out of hole
    #  4. Grab peg with gripper
    #  5. Move peg to goal
    # First, put the gripper mostly above the peg, so that we don't push it down
    # while trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # If the gripper isn't above the hole, drop it down the hole.
    if check("the robot's gripper is not above hole"):
        robot.drop("gripper down hole")
    # If the gripper is near the peg, we might be able to push the peg out of the
    # hole.
    if check("the robot's gripper is near peg and the peg is below the robot's gripper"):
        robot.push("peg up out of hole")
    # If the peg is above the gripper, we might be able to grab the peg with the
    # gripper.
    if check("the peg is above the robot's gripper and the robot's gripper is open"):
        robot.close("gripper around peg")     
    # Close the gripper to make sure we keep control of the peg.
    # Then we can move the peg to the goal.
    if check("the robot gripper is above the peg and the robot's gripper is closed"):
        robot.move("peg to goal")