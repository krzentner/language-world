# Steps:
    #  1. Put gripper above stick
    #  2. Grab stick with the gripper
    #  3. Put the other end of the stick above the thermos
    #  4. Push the thermos to target location using the stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # Grab the stick with the gripper
    if check("the robot's gripper is above the stick and the robot's gripper is open"):
        robot.move_gripper("around the stick", close_gripper=True)
    # Put the other end of the stick above the thermos
    if check("the stick is not above the thermos"):
        robot.move_gripper("above the thermos")
    # Push the thermos to target location using the stick
    if check("the stick is above the thermos and the thermos is not at the target location"):
        robot.move_gripper("near the target location")