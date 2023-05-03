if check("the robot's gripper is not holding the stick and the stick is not close to the thermos"):
        robot.grab("the stick")
    if check("the stick is close to the thermos and the thermos is not on the target location"):
        robot.pull("the thermos towards the target location")
    if check("the thermos is on the target location"):
        robot.release("the stick")