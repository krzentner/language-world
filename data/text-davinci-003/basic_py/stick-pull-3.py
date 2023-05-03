
    if check("the robot's gripper is not near the stick"):
        robot.grab("stick")
    if check("the thermos is right of the robot's gripper and the thermos is not near the stick"):
        robot.pull("the thermos near the stick")
    if check("the thermos is near the stick and the thermos is not horizontally aligned with the target location"):
        robot.align("the thermos with the target location")
    if check("the thermos is horizontally aligned with the target location"):
        robot.pull("the thermos towards the goal")