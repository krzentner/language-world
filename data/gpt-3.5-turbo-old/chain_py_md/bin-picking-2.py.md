# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):
    # Steps:
    #  1. Move the robot's gripper above the cube
    #  2. Move the robot's gripper around the cube
    #  3. Close the robot's gripper around the cube
    #  4. Lift the robot's gripper and cube
    #  5. Move to the target bin
    #  6. Move the robot's gripper above the target bin
    #  7. Release the cube into the target bin

    # First, put the robot's gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move("gripper above cube")
    # If the robot's gripper is not around the cube and open, move it to the
    # cube and close the gripper.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move("gripper around cube")
        robot.close("gripper around cube")
    # If the robot's gripper is closed around the cube and below its destination,
    # lift the cube.
    if check("the robot's gripper is closed around cube and not near the target bin"):
        robot.lift("gripper with cube")
    # Move the gripper and cube to the target bin.
    if check("the robot's gripper is not above the target bin"):
        robot.move("gripper to target bin")
    # If the gripper is above the target bin, release the cube.
    if check("the gripper is above the target bin and the robot's gripper is closed around cube"):
        robot.release("cube into target bin")