
    if check("the robot's gripper is not near cube and the robot's gripper is open"):
        robot.put("gripper near cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is closed and the cube is not near the target bin"):
        robot.move("cube to bin")
    if check("the cube is near the target bin and the robot's gripper is closed"):
        robot.place("cube in bin")