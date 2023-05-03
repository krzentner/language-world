
    if check("the robot's gripper is not almost vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("the stick is not forward aligned with the robot's gripper and the robot's gripper is open"):
        robot.grab("the stick")
    if check("the robot's gripper is forward aligned with the stick and the stick is not near the thermos"):
        robot.put("stick near thermos")
    if check("thermos is near stick and the stick is not pushing thermos"):
        robot.push("stick pushing thermos")
    if check("thermos is pushing by the stick"):
        robot.move("stick toward goal")