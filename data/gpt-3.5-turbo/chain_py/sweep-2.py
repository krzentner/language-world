# Steps:
    #  1. Put gripper near one side of the cube
    #  2. Grab the cube with the gripper
    #  3. Move the gripper sideways towards the goal while holding the cube
    # First, put the gripper near one side of the cube.
    if check("the robot's gripper is not near cube"):
        robot.move("gripper to one side of cube")
    # If the gripper is near the cube but not around it, drop the gripper around
    # the cube to grab it.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is around the cube, move it sideways to the target location
    # while holding the cube.
    if check("the robot's gripper is around cube"):
        robot.slide("gripper sideways to goal while holding cube")