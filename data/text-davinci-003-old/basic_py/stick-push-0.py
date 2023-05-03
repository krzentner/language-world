
    if check("the robot's gripper is not near the stick"):
        robot.grab("stick")
    if check("the robot's gripper is above the thermos but below the stick"):
        robot.reach("above thermos")
    if check("the robot's gripper is above the stick"):
        robot.push("stick onto thermos")
    if check("the robot's gripper is near the thermos and the robot's gripper has stick across it"):
        robot.push("thermos toward goal")