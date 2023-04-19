# Steps:
    #  1. Put gripper above the cube
    #  2. Move the gripper down around the cube from the side
    #  3. Close the gripper around the cube
    #  4. Lift the gripper and move it to the target location
    #  5. Drop the cube at the target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # Then, move the gripper down around the cube from the side.
    if check("the robot's gripper is not around cube"):
        robot.move_gripper("near the cube", "horizontally aligned with the cube", close_gripper=True)
    # Once the gripper is around the cube, lift and move it to the target location.
    if check("the robot's gripper is around cube and the robot's gripper is not vertically aligned with the target location"):
        robot.move_gripper("vertically aligned with the target location", close_gripper=True)
    # Finally, drop the cube at the target location.
    if check("the robot's gripper is vertically aligned with the target location and the robot's gripper is closed"):
        robot.move_gripper("above the target location")