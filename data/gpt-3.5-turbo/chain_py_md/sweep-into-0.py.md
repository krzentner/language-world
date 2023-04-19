# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    #  1. Put the gripper above and open
    #  2. Place the gripper around the cube
    #  3. Close the gripper around the cube
    #  4. Move the cube to the target location
    # First, put the gripper roughly above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, grab it by closing the gripper.
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # Move the cube to the target location while keeping the gripper closed.
    if check("the cube is held by the robot's gripper"):
        robot.place("cube at goal")