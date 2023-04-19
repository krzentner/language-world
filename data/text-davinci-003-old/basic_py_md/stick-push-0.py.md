

    if check("the robot's gripper is not near the stick"):
        robot.reach("stick")
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.drop("gripper around the stick")
    if check("the robot's gripper is forward aligned with the stick and the robot's gripper is closed"):
        robot.push("stick forward")
    if check("the robot's gripper and the stick are forward aligned and the stick is not near the thermos"):
        robot.slide("stick to thermos")
    if check("the robot's gripper is near the thermos and the stick is near the thermos"):
        robot.push("stick into thermos")
    if check("the robot's gripper is near the thermos and the stick is pushing the thermos"):
        robot.slide("the thermos to goal")