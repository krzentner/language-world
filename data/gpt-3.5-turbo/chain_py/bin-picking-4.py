# Steps:
    #  1. Identify the cube among other objects
    #  2. Put gripper above the cube
    #  3. Drop gripper around the cube
    #  4. Close gripper around the cube
    #  5. Move the cube to the target bin
    #  6. Drop the cube in the bin
    # First, use object recognition to identify the cube among other objects.
    if check("the robot does not see the cube"):
        robot.look("for the cube")
    # If the robot can see the cube, put the gripper above it.
    if check("the robot sees the cube and the gripper is not above the cube"):
        robot.put("gripper above the cube")
    # If the gripper is above the cube, drop it around the cube.
    if check("the gripper is above the cube and the gripper is not around the cube"):
        robot.drop("gripper around the cube")
    # If the gripper is around the cube, close the gripper around the cube.
    if check("the gripper is around the cube and the gripper is open"):
        robot.close("gripper around the cube")
    # If the gripper is closed around the cube, move the cube to the target bin.
    if check("the gripper is closed around the cube" and "the robot is not near the target bin"):
        robot.move("the cube to the target bin")
    # If the robot is near the target bin with the cube in the gripper, drop it
    # in the bin.
    if check("the robot is near the target bin and the gripper is closed around the cube"):
        robot.drop("the cube in the bin")