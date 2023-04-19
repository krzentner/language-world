

Steps: 
1. Put gripper above cube
2. Drop gripper around cube
3. Close gripper around cube
4. Line up the cube with its target bin 
5. Move the cube into bin 

# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Line up the cube with its target bin
    #  5. Move the cube into bin
    # First put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move_gripper("above the target bin")
    # If the robot's gripper is lined up above the bin, we can line up the cube
    # with the bin by changing the orientation of the gripper.
    if check("the robot's gripper is above target bin"):
        robot.move_gripper("near the target bin")
    # If the cube is lined up with the bin, move the cube into the bin.
    if check("the cube is horizontally aligned with bin"):
        robot.move_gripper("above the bin")