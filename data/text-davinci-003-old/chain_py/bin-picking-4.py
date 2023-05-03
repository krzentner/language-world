
    # Steps:
    #  1. Drop the gripper around the cube
    #  2. Close the gripper around the cube
    #  3. Move the cube to the target bin
    # We need to line up the gripper with the cube first.
    # If the gripper is not in the same vertical plane as the cube, we should
    # move the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with cube"):
        robot.place("gripper above cube")
    # If the gripper is now above the cube, we should push down with the gripper
    # to close it around the cube.
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not around the cube"):
        robot.put("gripper around cube")
    # Once the gripper is closed around the cube, we can move the cube to the
    # target bin.
    if check("the robot's gripper is around the cube"):
        robot.place("cube in bin")