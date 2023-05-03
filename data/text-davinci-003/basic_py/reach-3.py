
    if check("the robot's gripper is far from the target and the robot's gripper is not above the target"):
        robot.put("the gripper above the target")
    if check("the robot's gripper is above the target and the robot's gripper is not near the target"):
        robot.move("the gripper closer to the target")
    if check("the robot's gripper is near the target"):
        robot.pick("up the target")