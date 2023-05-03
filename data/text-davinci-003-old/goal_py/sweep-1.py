
    # Steps:
    #  1. Put gripper roughly above cube
    #  2. Drop gripper around cube
    #  3. Slide cube sideways
    #  4. Move cube to goal
    # First, put the gripper nowhere near the cube. We don't want to bump the cube
    # while trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube yet, let go of the cube.
    # Again, because the cube is small, don't worry about the direction.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # As long as the gripper is still low down, slide the cube sideways.
    # Don't move the gripper up too high, as that can bump the cube.
    if check("the robot's gripper is near the cube and the robot's gripper is not high above the cube"):
        robot.move_gripper("horizontally aligned with the target location")