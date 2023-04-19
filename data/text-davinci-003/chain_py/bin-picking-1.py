
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to target bin
    # Put the gripper above the cube.
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # As long as the gripper is lined up above the cube, we should be able to
    # lower the gripper onto the cube to grab it.
    if check("the robot's gripper is above cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube, close the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # Now that the cube is in the gripper, we can move it to the target bin.
    if check("the robot's gripper is around cube"):
        robot.place("cube in target bin")