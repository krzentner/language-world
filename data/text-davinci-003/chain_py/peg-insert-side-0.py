
    # Steps:
    #  1. Move the gripper above the peg
    #  2. Move the gripper to the left, around the peg
    #  3. Push the peg away from the gripper
    #  4. Move the peg and the gripper into the hole
    # First, move the gripper above the peg.
    # This should make it easier to grab the peg from the side.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # Drop the gripper down to the peg, so that we can grab it.
    # Be careful not to bump the peg while doing this.
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.put("gripper around the peg")
    # Grab the peg by putting the gripper around it.
    if check("the robot's gripper is around the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # Once it is grabbed, we can start pushing the peg away from the gripper and
    # towards the hole.
    if check("the robot's gripper is around the peg and the robot's gripper is closed"):
        robot.push("peg away from gripper")
    # Finally, we can move the gripper and the peg towards the hole.
    if check("the peg is away from the gripper and the peg is not near the hole"):
        robot.move("gripper and peg into hole")