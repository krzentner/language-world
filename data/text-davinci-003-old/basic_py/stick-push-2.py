
    if check("the robot's gripper is not near the stick"):
        robot.grab("stick")
    if check("the robot's gripper is near the stick and the stick is not near the thermos"):
        robot.put("stick near thermos")
    if check("the stick is near the thermos and the thermos is not horizontal to the robot's gripper"):
        robot.align("stick with thermos")
    if check("stick is horizontal to robot's gripper and the thermos is below the stick"):
        robot.push("stick away from robot")