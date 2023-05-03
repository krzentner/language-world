
    # Steps:
    #  1. Line up gripper along the side of the cube
    #  2. Push gripper into cube
    #  3. Push cube towards bin
    # First, line up the gripper along the side of the cube.
    # If the gripper isn't near the cube, move it over to it.
    if check("the robot's gripper is not along the side of the cube"):
        robot.move("gripper along side of cube")
    # If the gripper isn't inside the cube, push it into the cube.
    if check("the robot's gripper is not inside the cube"):
        robot.push("gripper into cube")
    # If the gripper is in the cube and the cube is not near the bin, push it
    # towards the bin.
    if check("the robot's gripper is inside the cube and the cube is not near the bin"):
        robot.push("cube towards bin")
    # If the cube is near the bin, move the cube so that it's in the bin.
    if check("the cube is near the bin"):
        robot.place("cube in bin")