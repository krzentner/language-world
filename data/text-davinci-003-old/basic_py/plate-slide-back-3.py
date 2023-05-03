
    if check("the robot's gripper is not above plate and the robot's gripper is not vertically aligned with plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not near plate"):
        robot.push("gripper into the plate")
    if check("the robot's gripper is near the plate and the plate is above the robot's gripper"):
        robot.slide("plate to target")