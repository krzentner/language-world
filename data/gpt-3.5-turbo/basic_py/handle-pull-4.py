if check("the robot's gripper is not above the handle and the robot's gripper is not vertically aligned with the handle"):
        robot.put("the gripper above the handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.pull("up on handle")