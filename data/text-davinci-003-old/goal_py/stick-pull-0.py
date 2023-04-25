
    # Steps:
    #  1. Put the gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Place the stick against the thermos
    #  4. Pull the thermos towards the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # Now that the gripper is around the stick, place it against the thermos.
    if check("the robot's gripper is around stick and the stick is not placed against thermos"):
        robot.move_gripper("against the thermos")
    # Finally, pull the thermos towards the target location.
    if check("the robot's gripper is against the thermos"):
        robot.move_gripper("near the target location")