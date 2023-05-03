# Steps:
    #  1. Put gripper above cube
    #  2. Grab cube with gripper
    #  3. Move gripper and cube to target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # Once the gripper is around the cube, move it to the target location.
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("near the target location")