# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):
    # Steps:
    #  1. Move gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Lift cube
    #  5. Move gripper above target bin
    #  6. Move gripper down towards bin
    #  7. Open gripper to drop cube into bin
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
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
    # Lift the cube up.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.lift("cube")
    # Move the gripper above the target bin.
    if check("the robot's gripper is not above the target bin"):
        robot.place("gripper above target bin")
    # Move the gripper down towards the bin.
    if check("the robot's gripper is above target bin and the robot's gripper is holding the cube"):
        robot.move("gripper down towards bin")
    # Once the gripper is near the bin, open it to drop the cube.
    if check("the robot's gripper is near target bin"):
        robot.open("gripper to drop cube into bin")