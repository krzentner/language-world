# Steps:
    #  1. Find cube using vision system
    #  2. Move gripper above the cube
    #  3. Drop gripper around the cube
    #  4. Close gripper around the cube
    #  5. Move the cube to the target bin
    #  6. Open gripper to release the cube
    # First, use the vision system to locate the cube.
    cube_location = robot.vision.detect_cube()
    # If the cube cannot be located, return False to indicate failure.
    if cube_location is None:
        return False
    # Move the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move("gripper to cube location")
    # Drop the gripper around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # Close the gripper around the cube.
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # Move the cube to the target bin.
    if check("the robot's gripper is closed and the cube is not in the target bin"):
        robot.move("gripper to bin location")
        robot.place("cube in the bin")
    # Open the gripper to release the cube.
    if check("the robot's gripper is closed and the cube is in the target bin"):
        robot.open("gripper")
    # Return True to indicate success.
    return True