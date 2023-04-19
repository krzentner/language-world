
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Grab the cube with gripper
    #  4. Move cube sideways to target location
    # Put the gripper at first above the cube.
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # If the gripper is above the cube, but not around it, drop the gripper
    # around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube but not around it, close the gripper
    # around the cube.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # Now that the cube is grabbed and lifted, we can move it to the target
    # location.
    if check("the robot's gripper is closed and cube is lifted above the robot's gripper"):
        robot.move("cube to target")