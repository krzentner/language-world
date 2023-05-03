# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above the cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around the cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around the cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed and the robot's gripper is not vertically aligned with the target bin"):
        robot.move("gripper above the target bin")
    if check("the robot's gripper is vertically aligned with the target bin and the robot's gripper is closed"):
        robot.release("the cube into the target bin")