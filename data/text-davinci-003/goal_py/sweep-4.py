
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Slide the cube sideways to the goal
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # If the cube becomes right of the gripper, go back to putting the gripper
    # above the cube.
    # Because the cube is a small object, check if the gripper is nearly around
    # it instead of checking if it's aligned with it from the front.
    if check("cube is not right of the robot's gripper and cube is not almost vertically aligned with the robot's gripper"):
        robot.move_gripper("almost vertically aligned with the cube", close_gripper=True)
    # Now that we have the cube, start pushing it side to side.
    if check("the robot's gripper is almost vertically aligned with cube"):
        robot.move_gripper("right of the cube")
    # Finally, as long as the robot's gripper is still near the cube, move it to
    # the target location.
    if check("the robot's gripper is near the cube"):
        robot.move_gripper("near the target location")