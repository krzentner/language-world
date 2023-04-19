# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Lift cube up
    #  5. Move gripper to target location
    #  6. Lower cube down
    # First, put the gripper roughly above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to lift the cube up.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.lift("cube up")
    # Move the gripper to the target location.
    if check("the robot's gripper is above target location and the cube is in the gripper"):
        robot.move("gripper to target location")
    # Lower the cube down to complete the task.
    if check("the gripper is near target location but above it with the cube in the gripper"):
        robot.lower("cube down")