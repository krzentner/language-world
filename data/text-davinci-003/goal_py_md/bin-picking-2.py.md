

Steps:
 1. Put the gripper above the cube
 2. Drop the gripper around the cube
 3. Close the gripper around the cube
 4. Move the cube towards the bin
 5. Drop the cube into the bin

# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):
    # Steps:
     1. Put the gripper above the cube
     2. Drop the gripper around the cube
     3. Close the gripper around the cube
     4. Move the cube towards the bin
     5. Drop the cube into the bin
    # Put the gripper above the cube. 
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, try to put it around the cube.
    if check("the robot's gripper is not around cube"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is around the cube, but not closed, try to close it around
    # the cube.
    if check("the robot's gripper is around the cube and the gripper is not closed"):
        robot.move_gripper("near the cube", close_gripper=True)
    # Now that we've closed the gripper, we can start moving the cube.
    if check("the robot's gripper is closed around the cube and the cube is not near the target bin"):
        robot.move_gripper("near the bin")
    # Once the cube is near the target bin, drop it in.
    if check("the robot's gripper is closed around the cube and the cube is near the target bin"):
        robot.move_gripper("above the bin", close_gripper=False)