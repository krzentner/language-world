
    if check("the robot's gripper is not above the stick"):
        robot.grab("stick")
    if check("the robot's gripper is above the stick"):
        robot.put("tip of stick below thermos")
    if check("the stick is below the thermos"):
        robot.push("thermos to goal")