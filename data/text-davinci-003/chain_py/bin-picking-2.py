
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Put cube in the target bin
    # First, put the gripper roughly above the cube, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not almost vertically aligned with the cube"):
        robot.put("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.grab("cube from above")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the cube to the target bin.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is closed and cube is near gripper"):
        robot.place("cube in target bin")