# sweep: grab the cube and move it sideways to the target location
# def sweep(robot):
    # Steps:
    #  1. Put the gripper above the cube
    #  2. Grab the cube
    #  3. Move the gripper and the cube sideways to the target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not aligned vertically with the cube"):
        robot.put("gripper above cube")
    # If the gripper is above the cube, close it to grab the cube.
    if check("the robot's gripper is above the cube and the gripper is open"):
        robot.grab("the cube")
    # Once we have the cube, move it to the target location horizontally, 
    # keeping the gripper above it.
    if check("the gripper has the cube and is not at the target location"):
        robot.move("the gripper and the cube to the target location sideways")