# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    # 1. Navigate the gripper above the bin
    # 2. Move the gripper down inside the bin
    # 3. Open the gripper to pick up the cube
    # 4. Move the gripper with the cube inside it towards the target bin
    # 5. Move the gripper down inside the target bin
    # 6. Release the cube inside the target bin
    # First, navigate the gripper above the bin.
    if check("the robot's gripper is not above the bin"):
        robot.place("gripper above bin")
    # Next, move the gripper down inside the bin.
    if check("the robot's gripper is not inside the bin"):
        robot.put("gripper inside bin")
    # Open the gripper to pick up the cube.
    if check("the cube is not inside the gripper"):
        robot.open("gripper")
    # Move the gripper with the cube inside it towards the target bin.
    if check("the robot's gripper is not above the target bin"):
        robot.place("gripper above target bin")
    # Move the gripper down inside the target bin.
    if check("the robot's gripper is not inside the target bin"):
        robot.put("gripper inside target bin")
    # Release the cube inside the target bin.
    if check("the cube is inside the gripper"):
        robot.open("gripper")