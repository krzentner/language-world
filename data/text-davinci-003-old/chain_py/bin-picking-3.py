
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Lift cube up
    #  5. Move gripper to bin
    #  6. Put cube in the bin
    # First, put the gripper above the cube, so that we know where it is.
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
    # Let's try to lift up the cube.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.lift("cube up")
    # We were able to lift the cube up with the gripper, so we should move it to
    # the bin.
    if check("the cube is lifted up in the robot's gripper"):
        robot.move("gripper to bin")
    # The gripper is near the bin, so we can just put the cube down.
    if check("the robot's gripper is near the bin and the cube is lifted in the robot's gripper"):
        robot.put("down the cube in the bin")