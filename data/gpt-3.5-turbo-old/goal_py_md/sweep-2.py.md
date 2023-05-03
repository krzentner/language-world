# sweep: grab the cube and move it sideways to the target location
# def sweep(robot):
    # Steps:
    # 1. Put the gripper above the cube
    # 2. Close the gripper around the cube
    # 3. Move the gripper in a sideways direction to the target location
    # First, we need to put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is around the cube, we can move it to the target location.
    if check("the robot's gripper is around the cube and the robot's gripper is not near the target location"):
        robot.move_gripper("left of the target location") # Move the gripper to the left of the target location
        if check("the robot's gripper is not near the target location"): # Check if the gripper has reached the target location
            robot.move_gripper("above the target location") # Move the gripper above the target location
    # Once the gripper is near the target location, release the cube.
    if check("the robot's gripper is near the target location and the gripper is closed around the cube"):
        robot.move_gripper("near the cube", close_gripper=False)