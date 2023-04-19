
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab the cube with the gripper
    #  3. Swing the cube to the target
    #  4. Drop the cube at the target
    # First, align the gripper with the cube from above.
    if check("the robot's gripper is not vertically aligned with cube"):
        robot.move_gripper("vertically aligned with the cube", close_gripper=True)
    # Once the robot's gripper is in line, grab the cube by closing the gripper.
    if check("the robot's gripper is vertically aligned with cube"):
        robot.move_gripper("near the target location")
    # Once the robot has grabbed the cube, a quick swinging motion will move it
    # to the target location.
    if check("the robot's gripper is near the target location and the robot's gripper is carrying cube"):
        robot.move_gripper("over the target location", close_gripper=False)