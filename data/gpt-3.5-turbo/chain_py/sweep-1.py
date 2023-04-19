# Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the cube to the left or right of the robot
    #  4. Move the cube to the target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # If the gripper is above the cube, grab it.
    if check("the robot's gripper is above the cube and the robot's gripper is open"):
        robot.grab("cube")
    # If the gripper is holding the cube, move it left or right based on the
    # current location of the cube.
    # Assume we want to move the cube to the right side of the robot first.
    if check("the robot's gripper is holding the cube and the cube is not on the right side of the robot"):
        robot.move("cube to the right of the robot")
    # If the cube is on the right side of the robot, move it to the target location.
    if check("the cube is on the right side of the robot"):
        robot.slide("cube to the goal")