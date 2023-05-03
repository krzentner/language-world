
    if check("the robot's gripper is not vertically aligned with hammer handle"):
        robot.put("gripper above hammer handle")
    if check("the robot's gripper is vertically aligned with hammer handle and the robot's gripper is open"):
        robot.put("gripper around hammer handle")
    if check("the robot's gripper is closed and the robot's gripper is forward aligned with the hammer handle and the hammer is not above the nail"):
        robot.align("hammer with nail")
    if check("the hammer is above the nail and the robot's gripper is vertically aligned with the hammer handle"):
        robot.hammer("down on nail")