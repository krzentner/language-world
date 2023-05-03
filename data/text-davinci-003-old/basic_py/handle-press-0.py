
    if check("the robot's gripper is not horizontally aligned with the handle and the robot's gripper is not above the handle"):
        robot.put("gripper above the handle")
    if check("the robot's gripper is near the handle and the robot's gripper is not horizontally aligned with the handle"):
        robot.align("gripper to handle")
    if check("the robot's gripper is horizontally aligned with the handle"):
        robot.push("down on handle")