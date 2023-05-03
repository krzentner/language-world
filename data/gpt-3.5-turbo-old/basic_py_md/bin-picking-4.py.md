# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):
def bin_picking(robot):
    if check("cube is not in the gripper and the gripper is not above the cube"):
        robot.reach("to cube")
    if check("the gripper is above the cube and the gripper is not closed"):
        robot.close("gripper around cube")
    if check("the cube is in the gripper and the gripper is not above the target bin"):
        robot.reach("to bin")
    if check("the gripper is above the target bin"):
        robot.place("cube in bin")