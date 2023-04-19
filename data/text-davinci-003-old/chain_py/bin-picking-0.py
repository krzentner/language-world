
    # Steps:
    #  1. Put the gripper above the cube
    #  2. Drop the gripper around the cube
    #  3. Close the gripper around the cube
    #  4. Move the cube to the bin
    #  5. Place the cube in the bin
    # First, put the gripper roughly above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the cube to the bin.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move("cube to bin")
    # If the cube is near the bin, place it in the bin.
    if check("the cube is near the bin"):
        robot.place("cube in bin")