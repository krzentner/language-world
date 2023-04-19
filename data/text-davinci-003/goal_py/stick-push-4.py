
    # Steps:
    #  1. Put the robotic gripper right of the stick
    #  2. Grab the stick with the robotic gripper
    #  3. Line the stick above the thermos
    #  4. Push the thermos with the stick
    # If the robot's gripper is not near the stick to grab it, move it there.
    if check("the robot's gripper is not near the stick"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the stick is not above the thermos, line it up above the thermos.
    if check("the robot's gripper is near the stick and the stick is not above the thermos"):
        robot.move_gripper("above the thermos")
    # If the stick is above the thermos and not in contact with it, push it with
    # the stick.
    if check("the stick is above the thermos and the stick is not in contact with the thermos"):
        robot.move_gripper("near the target location")