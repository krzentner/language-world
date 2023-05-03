
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Move stick to thermos
    #  5. Use the stick to push the thermos
    # First, put the gripper roughly above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # When the gripper has the stick, move it close to the thermos.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("near the thermos")
    # Finally, push the thermos with the stick.
    if check("the robot's gripper is near the thermos"):
        robot.move_gripper("horizontally aligned with the thermos")