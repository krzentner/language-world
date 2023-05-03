# Steps:
    #  1. Put the gripper above the hole
    #  2. Line up the gripper with the peg
    #  3. Grab the peg with the gripper
    #  4. Lift the peg out of the hole
    #  5. Move the peg to the target location
    # First, put the gripper above the peg hole.
    if check("the robot's gripper is not vertically aligned with the hole"):
        robot.put("gripper above hole")
    # Align the gripper with the peg so that we can grab it.
    if check("the peg is not forward aligned with the robot's gripper" and "the peg is not left of the robot's gripper"):
        robot.align("peg with gripper")
    # Grab the peg with the gripper once it's aligned.
    if check("the peg is forward aligned with the robot's gripper and the peg is left of the robot's gripper"):
        robot.grab("peg")
    # Move the gripper up to lift the peg out of the hole.
    if check("the gripper is around the peg"):
        robot.lift("peg out of hole")
    # Move the peg to the target location.
    if check("the gripper is holding the peg above the hole"):
        robot.move("peg to goal location")