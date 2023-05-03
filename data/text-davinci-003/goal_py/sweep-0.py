
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Sweeping motion to sweep cube to goal
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above cube and the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # Once the gripper is lined up with the cube, grab the cube with the gripper.
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # Now that the cube is grabbed, we can do a sweeping motion to move the cube
    # sideways to the target location.
    if check("the robot's gripper is near cube and the robot's gripper is closed"):
        robot.move_gripper("horizontally aligned with the target location")