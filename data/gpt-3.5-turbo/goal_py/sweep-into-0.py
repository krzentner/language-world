# Steps:
    #  1. Put gripper above and to the side of the cube
    #  2. Move gripper down around one side of the cube
    #  3. Grab the cube
    #  4. Move gripper to the target location while holding the cube
    #  5. Release the cube
    # First, put the gripper above and to the side of the cube, to avoid hitting
    # it while grabbing it.
    if check("the robot's gripper is not above and to the side of the cube"):
        robot.move_gripper("above and to the side of the cube")
    # Move the gripper down around the side of the cube, to grab it.
    if check("the robot's gripper is not around the cube and the gripper is above the cube"):
        robot.move_gripper("around the cube")
    # Once the gripper is around the cube, grab it.
    if check("the robot's gripper is around the cube and the gripper is open"):
        robot.move_gripper("above the target location", close_gripper=True)
    # Once the gripper is holding the cube, move it to the target location.
    if check("the robot's gripper is above the target location and the gripper is closed around the cube"):
        robot.move_gripper("near the target location")
    # Once the gripper is near the target location, release the cube.
    if check("the robot's gripper is near the target location and the gripper is closed around the cube"):
        robot.move_gripper("above the target location", close_gripper=False)