

if check("the robot's gripper is not near the stick"):
    robot.grab("stick")
if check("the robot's gripper is not near thermos and the stick is not above the thermos"):
    robot.put("stick above thermos")
if check("the stick is above the thermos and the robot's gripper is not forward aligned with the thermos"):
    robot.align("stick with thermos")
if check("the stick is forward aligned with the thermos and the robot's gripper is near the thermos"):
    robot.push("stick forward")