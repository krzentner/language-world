
    if check("the robot's gripper is not vertically aligned with the nail"):
        robot.put("gripper near the nail")
    if check("the robot's gripper is vertically aligned with nail and the robot's gripper is not near hammer"):
        robot.pick_up("hammer")
    if check("the robot's gripper is above hammer and the robot's gripper is not near nail"):
        robot.put("hammer near nail")
    if check("the hammer is near the nail"):
        robot.hammer("nail")