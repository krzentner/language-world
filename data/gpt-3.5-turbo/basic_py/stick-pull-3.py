if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above the stick")
    if check("stick is not left of the robot's gripper and stick is not forward aligned with the robot's gripper"):
        robot.grab("stick")
    if check("the robot's gripper is forward aligned with the stick"):
        robot.pull("thermos with stick")
    if check("the robot's gripper is near the goal and the thermos is stuck"):
        robot.push("thermos with stick harder")