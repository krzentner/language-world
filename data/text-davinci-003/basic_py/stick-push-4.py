
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    if check("the robot's gripper is above the stick and the robot's gripper is open"):
        robot.grab("stick")
    if check("the robot's gripper is closed and the stick is not above the thermos"):
        robot.align("stick to thermos")
    if check("the stick is above the thermos"):
        robot.push("thermos to goal")