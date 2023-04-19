
    # Steps:
    #  1. Put gripper near cube 
    #  2. Grasp cube with gripper
    #  3. Lift cube
    #  4. Move to bin
    #  5. Place cube in bin
    # First, position the gripper above the cube. This makes it easier to
    # position it correctly for grasping the cube.
    if check("the robot's gripper is not near the cube"):
        robot.put("gripper near cube")
    # Once the gripper is near the cube, grab it with the gripper.
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.grab("cube")
    # Pick up the cube by lifting the gripper.
    if check("the robot's gripper is around the cube and the robot's gripper is closed"):
        robot.lift("cube")
    # Move the cube to the target bin.
    if check("the robot's gripper is carrying a cube"):
        robot.move("cube to bin")
    # Place the cube in the bin.
    if check("the robot's gripper is holding a cube and the cube is near the target bin"):
        robot.place("cube in bin")