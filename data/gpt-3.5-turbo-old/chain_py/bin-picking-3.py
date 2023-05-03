# Steps:
    #  1. Locate the cube
    #  2. Move gripper above the cube
    #  3. Grab the cube
    #  4. Move gripper above the target bin
    #  5. Drop the cube into the bin
    # First, locate the cube.
    if check("the cube is not in sight"):
        robot.locate("the cube")
    # Once the cube is located, move the gripper above it.
    if check("the robot's gripper is not above the cube"):
        robot.move("gripper above the cube")
    # Grab the cube if the gripper is around it.
    if check("the robot's gripper is around the cube and the gripper is open"):
        robot.close("the gripper around the cube")
    # Move the gripper above the target bin.
    if check("the robot's gripper is closed and the gripper is not above the target bin"):
        robot.move("gripper above the target bin")
    # Drop the cube into the target bin.
    if check("the robot's gripper is closed and the gripper is above the target bin"):
        robot.drop("the cube into the bin")