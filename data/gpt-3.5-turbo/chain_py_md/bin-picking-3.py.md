# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Find the cube in the bin
    #  2. Position the gripper around the cube
    #  3. Lift the cube out of the bin
    #  4. Move to the target bin
    #  5. Position the gripper above the target bin
    #  6. Lower the cube into the target bin
    
    # Find the cube in the bin.
    if check("the cube is not in sight"):
        robot.look("for the cube")
    # Position the gripper around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.put("gripper around cube")
    # Lift the cube out of the bin.
    if check("the robot's gripper is around cube and the robot's gripper is open"):
        robot.close("gripper around cube")
        robot.lift("cube out of the bin")
    # Move to the target bin.
    if check("the robot is not at the target bin"):
        robot.move("to the target bin")
    # Position the gripper above the target bin.
    if check("the robot's gripper is not above the target bin"):
        robot.put("gripper above the target bin")
    # Lower the cube into the target bin.
    if check("the robot's gripper is above the target bin and the robot's gripper is closed"):
        robot.lower("the cube into the target bin")