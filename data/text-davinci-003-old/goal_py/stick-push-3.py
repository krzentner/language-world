
    # Steps:
    #  1. Put gripper above the stick
    #  2. Pick up the stick
    #  3. Put the tip of the stick behind the thermos
    #  4. Push the thermos with the stick – rotate the gripper while pushing
    # First, put the gripper above the stick so that we can grab it.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # Now that the gripper is lined up above the stick, we should be able to
    # pick up the stick.
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is closed"):
        robot.move_gripper("vertically aligned with the thermos")
    # Once the tip of the stick is behind the thermos, we can push the thermos
    # by twisting the gripper while pushing.
    if check("the tip of the stick is behind thermos"):
        robot.move_gripper("above the target location")