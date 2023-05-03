
    # Steps:
    #  1. Put gripper left of the cube
    #  2. Close gripper around cube
    #  3. Sweep cube to the goal
    # Because the cube is small, we need to make sure we don't lose the cube and
    # put the gripper above the cube before closing it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the cube is too far left of the gripper, we should move the gripper
    # near the cube to start sweeping.
    if check("the robot's gripper is above the cube and the cube is not left of the robot's gripper"):
        robot.move_gripper("left of the cube")
    # Make sure that the cube is left of the gripper before starting the sweep.
    if check("the robot's gripper is left of the cube"):
        robot.move_gripper("above the target location")