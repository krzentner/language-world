if check("the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate"):
        robot.push("the gripper into the plate")
    if check("the robot's gripper is near the plate and the plate is not at the target location"):
        robot.slide("the plate back")