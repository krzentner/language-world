
    if check("the robot's gripper is not above the cube and the robot's gripper is not in the same plane as the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not around cube and the cube is not left of the robot's gripper"):
        robot.grab("cube")
    if check("the robot's gripper is around cube and the robot's gripper is not to the target bin"):
        robot.move("gripper to target bin")
    if check("the robot's gripper is almost vertically aligned with the bin and the robot's gripper is open"):
        robot.put("gripper into the bin")
    if check("the robot's gripper is vertically aligned with the bin"):
        robot.drop("cube in the bin")