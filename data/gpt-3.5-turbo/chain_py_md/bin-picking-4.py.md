# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):
    # Steps:
    #  1. Move gripper to above cube
    #  2. Check if cube is graspable
    #  3. Grasp the cube
    #  4. Lift the cube
    #  5. Move gripper above target bin
    #  6. Check if bin is reachable
    #  7. Release the cube into the bin
    # First, move the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move("gripper to above the cube")
    # Check if the cube is graspable. If it is not, move the gripper to a better
    # position.
    if check("the cube is not graspable"):
        robot.move("gripper to a better position")
    # Once the gripper is around the cube, grasp it.
    if check("the gripper is not grasping the cube"):
        robot.grasp("the cube")
    # After the gripper grasps the cube, lift it.
    if check("the gripper is holding the cube but not lifted off the table"):
        robot.lift("the cube")
    # Move the gripper above the target bin.
    if check("the gripper is not above the target bin"):
        robot.move("gripper to above the target bin")
    # Check if the bin is reachable. If not, move the gripper to a better
    # position.
    if check("the bin is not reachable"):
        robot.move("gripper to a better position")
    # Release the cube into the bin.
    if check("the gripper is above the target bin and holding the cube"):
        robot.release("the cube into the target bin")