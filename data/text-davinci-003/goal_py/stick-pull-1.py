
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Angle the stick into the thermos
    #  5. Push the thermos to the goal
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the stick isn't left of the gripper, move the gripper to the stick.
    if check(" sticky not left of the robot's gripper and the robot's gripper is not open"):
        robot.move_gripper("left of the stick", close_gripper=True)
    # If the gripper is opening the stick, angle the stick so it points into
    # the thermos.
    if check(" robot's gripper is open and the robot's gripper is forward aligned with the stick"):
        robot.move_gripper("angled towards the thermos")
    # If the stick is angled into the thermos, we can push the thermos to the
    # target location.
    if check("the robot's gripper is around the stick and the stick is pointing into the thermos"):
        robot.move_gripper("near the target location")