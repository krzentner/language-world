
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Put the stick in front of the thermos
    #  4. Push the thermos with the stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick", close_gripper=True)
    # Once the gripper is above the stick, we can grab it.
    # We can just line up the gripper from the front and close it.
    if check("the robot's gripper is forward aligned with the stick"):
        robot.move_gripper("in front of the thermos")
    # Now that the stick is in front of the thermos, we can push it.
    if check("the stick is in front of the thermos and the thermos is not near the target location"):
        robot.move_gripper("near the target location")