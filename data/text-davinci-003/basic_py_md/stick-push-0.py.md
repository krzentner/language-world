

if check("the robot's gripper is not near the stick and the stick is not horizontally aligned with the thermos"):
    robot.grab("stick")
if check("the robot's gripper is near the stick and the stick is not horizontally aligned with the thermos"):
    robot.align("stick above thermos")
if check("the robot's gripper is near the stick and the stick is horizontally aligned with the thermos"):
    robot.push("stick into thermos")
if check("the thermos is below the stick"):
    robot.push("stick towards goal")