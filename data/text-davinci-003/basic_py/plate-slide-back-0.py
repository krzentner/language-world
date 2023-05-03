
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is above the plate and the robot's gripper is open"):
        robot.drop("gripper onto the plate")
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.push("plate back")
    if check("the robot's gripper is forward aligned with the plate and the robot's gripper is open"):
        robot.close("gripper onto the plate")
    if check("the robot's gripper is near the plate and the robot's gripper is closed"):
        robot.pull("plate back to target")