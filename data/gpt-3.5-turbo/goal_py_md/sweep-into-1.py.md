# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    # 1. Put gripper above the cube
    # 2. Close gripper to grab the cube
    # 3. Move the cube to the target location by sliding it
    # First, put the gripper above the cube
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # If the gripper is near the cube, grab it by closing the gripper
    if check("the robot's gripper is above the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is holding the cube, slide it towards the target location
    if check("the robot's gripper is holding the cube and the cube is below the robot's gripper"):
        robot.move_gripper("above the target location")