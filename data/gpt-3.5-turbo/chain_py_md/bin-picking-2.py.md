# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Line up the gripper above the cube
    #  2. Drop the gripper around the cube
    #  3. Close the gripper around the cube
    #  4. Lift the cube out of the bin
    #  5. Move the gripper to the target bin
    #  6. Put the gripper above the target bin
    #  7. Drop the cube into the target bin
    #  8. Open the gripper
    
    # First, put the gripper roughly above the cube, so that we don't bump it while
    # trying to grab it.
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
    # Lift the cube out of the bin.
    if check("the robot's gripper is around cube"):
        robot.lift("cube out of bin")
    # Move the gripper to the target bin.
    if check("the robot's gripper is holding cube"):
        robot.move("gripper to target bin")
    # Put the gripper above the target bin.
    if check("the robot's gripper is near target bin"):
        robot.place("gripper above target bin")
    # If the gripper is above the bin, drop the cube into the bin.
    if check("the robot's gripper is above target bin"):
        robot.drop("cube into target bin")
    # Open the gripper.
    if check("the robot's gripper is holding cube above target bin"):
        robot.open("gripper")