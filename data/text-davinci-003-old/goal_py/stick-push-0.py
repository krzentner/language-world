
    # Steps:
    #  1. Put the gripper near the stick
    #  2. Close the gripper around the stick
    #  3. Push the stick against the thermos and move it
    # First, put the gripper near the stick.
    if check("the robot's gripper is not near stick"):
        robot.move_gripper("near the stick")
    # If the gripper is near the stick but not closed, close the gripper
    # around it.
    if check("the robot's gripper is near stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the gripper is closed around stick, put the stick near the thermos and
    # use the stick to move the thermos.
    if check("the robot's gripper is closed around stick and the robot's gripper is not near thermos"):
        robot.move_gripper("near the thermos")
    # If the thermos is near the stick, just push the thermos with the stick
    # towards the goal.
    if check("the robot's gripper is near thermos"):
        robot.move_gripper("near the goal")