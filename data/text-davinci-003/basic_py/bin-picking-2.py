
    if check("the robot's gripper is not above the cube"):
        robot.reach("to cube")
    if check("the robot's gripper is above the cube and the robot's gripper is wrinkled"):
        robot.straighten("gripper")
    if check("the robot's gripper is above the cube and the robot's gripper is not open"):
        robot.open("gripper")
    if check("the robot's gripper is above the cube and the robot's gripper is open"):
        robot.pick("up cube")
    if check("the robot's gripper is around the cube and the target bin is not forward aligned with the robot's gripper"):
        robot.align("bin forward with the gripper")
    if check("the target bin is forward aligned with the robot's gripper"):
        robot.place("cube in target bin")