

If check("the robot's gripper is not near the stick"):
    robot.reach("stick")
if check("the robot's gripper is near the stick and stick is not facing thermos"):
    robot.rotate("stick to face thermos")
if check("the robot's gripper is around the stick and stick is facing thermos"):
    robot.push("stick on thermos")
if check("the robot's gripper is around the stick and thermos is not at the target location"):
    robot.push("stick to goal")