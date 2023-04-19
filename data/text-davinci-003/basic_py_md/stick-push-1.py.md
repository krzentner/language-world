

If check("the robot's gripper is not above stick"):
    robot.put("gripper above stick")
if check("the robot's gripper is above stick and the robot's gripper is not around stick"):
    robot.drop("gripper around stick")
if check("the robot's gripper is around stick and the robot's gripper is not near thermos"):
    robot.push("stick towards thermos")
if check("the robot's gripper is near thermos and thermos is not below the robot's gripper"):
    robot.move("stick above thermos")
if check("the robot's gripper is near thermos and thermos is below the robot's gripper"):
    robot.slide("thermos to goal")