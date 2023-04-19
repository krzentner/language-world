
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube with the gripper
    #  3. Sweep into target location
    # We want the gripper to be higher than the cube when it grabs and sweeps,
    # so put the gripper a little above the cube.
    if check("the robot's gripper is not near cube and the robot's gripper is not above cube"):
        robot.place("gripper above cube")
    # If the gripper is above the cube and not touching it, reach down to it so
    # that the gripper grabs it.
    if check("the robot's gripper is above cube and the robot's gripper is not near cube"):
        robot.grab("cube")
    # If the gripper is near the cube, close the gripper around it.
    if check("the robot's gripper is near cube and the gripper is open"):
        robot.close("gripper around cube")
    # Once the cube is grabbed, just sweep it into the target location.
    if check("the robot's gripper is above cube and the gripper is closed"):
        robot.sweep("cube into goal")