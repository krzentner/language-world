# Steps:
    #  1. Put gripper above the hole
    #  2. Move the gripper down into the hole
    #  3. Grab the peg
    #  4. Lift the peg out of the hole
    #  5. Move the gripper to the target location
    # First we need to position the robot above the hole to grab the peg.
    if check("the robot's gripper is not above the hole"):
        robot.move_gripper("above the hole")
    # Once the gripper is above the hole, we can lower it to grab the peg.
    # We'll assume that the gripper is already closed when near the peg hole.
    if check("the robot's gripper is not inside the hole and the robot's gripper is closed"):
        robot.move_gripper("inside the hole")
    # Now that the gripper is around the peg, we need to lift it out of the hole.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("out of the hole")
    # Finally, we move the gripper to the target location.
    if check("the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")