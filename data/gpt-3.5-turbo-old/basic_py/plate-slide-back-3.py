if check("the robot's gripper is not above the plate and the plate is not blocked"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is above the plate and the plate is not blocked"):
        robot.push("the gripper into the plate")
    if check("the robot's gripper is near the target location"):
        robot.slide_back("the plate to the target location")