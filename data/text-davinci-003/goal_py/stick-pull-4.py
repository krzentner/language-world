
    # Steps:
    #  1. Put gripper in front of stick
    #  2. Grasp the stick
    #  3. Use stick to pull the thermos
    # First, put the gripper in front of the stick to start the pull.
    if check("the robot's gripper is not in front of the stick"):
        robot.move_gripper("in front of the stick", close_gripper=True)
    # If the stick isn't left of the gripper and we're not pulling the thermos,
    # pick up the stick.
    if check("the stick is not left of the robot's gripper and the thermos is not in front of the robot's gripper"):
        robot.move_gripper("left of the stick")
    # If the robot isn't already pulling the thermos, start pulling it.
    if check("the stick is left of the robot's gripper and the thermos is in front of the robot's gripper"):
        robot.move_gripper("in front of the target location")