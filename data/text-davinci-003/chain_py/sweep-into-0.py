
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Sweep with gripper down to target location
    # As with pick-place, the robot needs to trap the cube with the gripper to
    # move it.
    # First, move the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.position("gripper above cube")
    # Drop the gripper around the cube if it isn't closed around it yet.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # With the gripper around the cube, close the gripper to grab it.
    if check("the robot's gripper is around the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # With the cube grabbed, we can sweep it to the target location.
    if check("the robot's gripper is around the cube and the robot's gripper is closed"):
        robot.sweep("gripper down to target location")