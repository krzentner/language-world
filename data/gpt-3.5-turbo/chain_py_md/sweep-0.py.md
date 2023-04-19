# sweep: grab the cube and move it sideways to the target location
# def sweep(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube with gripper
    #  3. Move the gripper and cube sideways to the target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # Once the gripper is above the cube, close the gripper to grab the cube.
    if check("the robot's gripper is above the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # Now that the robot has the cube, move it laterally to the target location.
    if check("the robot's gripper is holding the cube and is not near the target location"):
        robot.move("the gripper and the cube sideways to the target location")