
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is above the mug and the robot's gripper is open"):
        robot.grab("mug")
    if check("the robot's gripper is around the mug and the mug is not near the target location"):
        robot.slide("mug to target location")
    if check("the mug is near the target location"):
        robot.stop("moving mug")