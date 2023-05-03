# Steps:
    # 1. Put the gripper above the cube
    # 2. Drop the gripper around the cube
    # 3. Close the gripper around the cube
    # 4. Move the cube to the target location
    # First, put the gripper roughly above the cube
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # If the gripper is not around the cube, move the gripper down around it.
    if check("the robot's gripper is above the cube and the robot's gripper is not around the cube"):
        robot.drop("gripper around cube")
    # If the gripper is around the cube and is still open, close it to grab the
    # cube.
    if check("the robot's gripper is around the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # Move the cube to the target location
    if check("the robot's gripper is closed with the cube and the cube is not at the target location"):
        robot.move("cube to target location")