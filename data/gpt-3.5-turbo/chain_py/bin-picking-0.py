# Steps:
    #  1. Move gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper to grab cube
    #  4. Move gripper to target bin
    #  5. Drop cube in target bin
    # First, move the gripper roughly above the cube.
    if check("the robot's gripper is not above cube"):
        robot.move("gripper above cube")
    # If the gripper isn't around the cube yet, move it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is not open"):
        robot.drop("gripper around cube")
    # If the gripper is around the cube, maybe we can grab it by closing the
    # gripper.
    if check("the robot's gripper is around cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # If the gripper is closed around the cube, move it to the target bin.
    if check("the robot's gripper is around cube and the robot's gripper is not at target bin"):
        robot.move("gripper to target bin")
    # Drop the cube in the target bin.
    if check("the robot's gripper is at target bin and the robot's gripper is closed"):
        robot.drop("cube in target bin")