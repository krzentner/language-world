# Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Line the gripper up with the target location
    #  4. Move the gripper to the target location, sliding the cube along
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # If the gripper isn't around the cube, move it down to grab the cube.
    if check("the robot's gripper is above the cube and the robot's gripper is not around the cube"):
        robot.move_gripper("around the cube", close_gripper=True)
    # Once the gripper is around the cube, align it with the target location.
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("above the target location")
    # Move the gripper to the target location, sliding the cube along.
    if check("the robot's gripper is aligned with the target location"):
        robot.move_gripper("vertically aligned with the target location")