# Steps:
    #  1. Put gripper above peg
    #  2. Grab the peg with the gripper
    #  3. Lift the peg out of the hole
    #  4. Move the peg to the target location
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the gripper is not around the peg, grab it.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.grab("peg")
    # Once the peg is grabbed, lift it out of the hole.
    if check("the robot's gripper is around peg and the peg is not lifted above the hole"):
        robot.lift("peg out of hole")
    # Finally, move the peg to the target location.
    if check("the peg is above the robot's gripper"):
        robot.move("peg to goal")