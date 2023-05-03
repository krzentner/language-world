if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("the robot's gripper is around stick and the stick is not touching thermos"):
        robot.push("stick towards thermos")
    if check("the stick is touching the thermos and the robot's gripper is not near thermos"):
        robot.grab("thermos")
    if check("the robot's gripper is near thermos and the thermos is below robot's gripper"):
        robot.pull("thermos to goal")