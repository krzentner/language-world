if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("stick is not left of the robot's gripper and stick is not forward aligned with the robot's gripper"):
        robot.grab("stick")
    if check("the robot's gripper is forward aligned with the stick and the stick is not near the thermos"):
        robot.align("stick to thermos")
    if check("the robot's gripper is around the stick and the stick is near the thermos"):
        robot.push("thermos with stick to goal")