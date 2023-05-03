
    if check("the robot's gripper is not near the stick and the stick is not near the thermos"):
        robot.reach("stick to thermos")
    if check("the stick is near the thermos and the robot's gripper is not near the stick"):
        robot.reach("gripper to stick")
    if check("the robot's gripper is near the stick"):
        robot.push("the stick onto the thermos")
    if check("the stick is touching the thermos"):
        robot.push("the thermos to task goal")