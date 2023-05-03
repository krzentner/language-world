
    if check("the robot's gripper is not forward aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is forward aligned with the puck and the robot's gripper is not near to the puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.backwards("the puck to the goal")