# Steps:
    #  1. Put the gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Position the gripper above the thermos, with the stick pointing towards it
    #  4. Push the thermos with the stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # Once the gripper is above the stick, close the gripper around it.
    if check("the robot's gripper is above the stick"):
        robot.move_gripper("around the stick")
    # Now that we have the stick, we need to position the gripper above the thermos,
    # with the stick pointing towards it.
    if check("the robot's gripper is not positioned above the thermos with the stick pointing towards it"):
        robot.move_gripper("above the thermos with the stick pointing towards it")
    # Once the gripper is positioned correctly, use the stick to push the thermos
    # to the target location
    if check("the robot's gripper is positioned above the thermos with the stick pointing towards it"):
        robot.move_gripper("above the target location with the stick pointing towards the thermos")