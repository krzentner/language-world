# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    #  1. Put the gripper above the cube
    #  2. Grab the cube
    #  3. Move the cube to the target location
    # First, put the gripper above the cube
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above the cube")
    # If the gripper is above the cube, grab the cube
    if check("the robot's gripper is above the cube and the robot's gripper is open"):
        robot.grab("the cube")
    # If the cube is grabbed, move it to the target location
    if check("the robot's gripper is holding the cube"):
        robot.move("the cube to the goal location")