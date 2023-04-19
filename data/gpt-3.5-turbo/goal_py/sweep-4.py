# Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the gripper and cube sideways to the target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # If the gripper is above the cube but not around it, put the gripper around
    # the cube.
    if check("the robot's gripper is above the cube but not around it and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is around the cube, we can move the gripper and cube
    # sideways to the target location.
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("near the target location")