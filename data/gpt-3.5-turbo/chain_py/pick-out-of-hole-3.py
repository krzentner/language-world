# Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Lift the peg out of the hole
    #  4. Move the peg to the target location
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg is in the gripper and the gripper is above the hole, lift the
    # peg out.
    if check("the robot's gripper is around peg and the peg is in the hole"):
        robot.lift("peg out of hole")
    # If the peg is out of the hole and the gripper is holding it, move the peg
    # to the target location.
    if check("the robot's gripper is around peg"):
        robot.move("peg to goal")