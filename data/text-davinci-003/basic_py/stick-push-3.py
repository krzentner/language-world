
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    if check("the stick is not left of the robot's gripper"):
        robot.grab("stick")
    if check("the robot's gripper is above the thermos"):
        robot.push("stick against the thermos")
    if check("the thermos is below the robot's gripper and the thermos is not at the goal"):
        robot.Move("thermos to goal")