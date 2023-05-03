# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.pick("up cube")
    if check("the robot's gripper is not aligned with bin and the gripper is holding the cube"):
        robot.put("gripper above bin")
    if check("the robot's gripper is vertically aligned with bin and the gripper is holding the cube"):
        robot.release("cube in bin")