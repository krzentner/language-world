
    # Steps:
    #  1. Put gripper left of the cube
    #  2. Grab hold of the cube
    #  3. Start sweeping the cube towards the target
    #  4. Keep sweeping the cube until it reaches the target
    # First, move the gripper next to the cube.
    if check("the robot's gripper is not left of the cube"):
        robot.move_gripper("left of the cube")
    # If the gripper is next to the cube, start sweeping the cube towards the
    # target.
    if check("the robot's gripper is left of the cube"):
        robot.move_gripper("in front of the cube")
    # Once the gripper is in front of the cube, grab it.
    if check("the robot's gripper is in front of cube and the robot's gripper is open"):
        robot.move_gripper("right of the cube", close_gripper=True)
    # Keep sweeping the cube towards the target until it reaches it.
