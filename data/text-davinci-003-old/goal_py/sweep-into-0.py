
    # Steps:
    #  1. Put gripper over cube
    #  2. Sweep the cube into the goal
    # First, put the gripper over the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # Grab the cube with the gripper.
    if check("the robot's gripper is above the cube"):
        robot.move_gripper("near the cube", close_gripper=True)
    # Now that the cube is in the gripper, sweep it into the goal.
    if check("the robot's gripper is above the cube and the cube is below the robot's gripper"):
        robot.move_gripper("near the target location")