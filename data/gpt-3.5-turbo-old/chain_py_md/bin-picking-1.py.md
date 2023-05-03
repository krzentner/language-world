# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):
    # Steps:
    #  1. Move gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Lift cube
    #  5. Move gripper to target bin
    #  6. Lower cube into target bin
    # First, move the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to lift the cube.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.lift("cube")
    # Move the gripper to the target bin.
    if check("the robot's gripper is holding the cube and the target bin is not near the robot's gripper"):
        robot.move("gripper to target bin")
    # Lower the cube into the target bin.
    if check("the robot's gripper is holding the cube and the cube is above the target bin"):
        robot.drop("cube into target bin")