# Steps:
    #  1. Find the cube
    #  2. Put gripper above cube
    #  3. Drop gripper around cube
    #  4. Close gripper around cube
    #  5. Move cube to target bin
    #  6. Open gripper to drop cube in bin
    # First, use the robot's sensors to find the cube.
    if check("cube not found"):
        robot.search("for cube")
    # Once the cube is found, put the gripper roughly above it.
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
    # Try to move the cube to the target bin.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.place("cube in target bin")
    # Once the cube is in the target bin, open the gripper to drop it.
    if check("the robot's gripper is above target bin and the robot's gripper is closed"):
        robot.open("gripper to drop cube")