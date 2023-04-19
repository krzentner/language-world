# sweep: grab the cube and move it sideways to the target location
# def sweep(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab the cube with the gripper
    #  3. Move the cube to the side
    #  4. Move the cube to the target location
    # First, put the gripper roughly above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.hit("the gripper to detect the cube location")
        robot.place("the gripper roughly above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the cube to the side.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move("cube to the side")
    # If the robot's gripper is on the side and not yet at the target location move it to the target location.
    if check("the robot's gripper is on the side of the cube and the robot's gripper is not at the target"):
        robot.move("cube to the target")