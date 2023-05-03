

if check("the robot's gripper is not near the stick"):
        robot.grab("the stick")
    if check("the robot's gripper is near the stick and the stick is not horizontally aligned with thermos top"):
        robot.align("the stick with the thermos")
    if check("the robot's gripper is near the stick and the stick is horizontally aligned with the thermos top"):
        robot.pull("the thermos to the target location")