if check("the robot's gripper is not holding the stick and the stick is not positioned behind the thermos"):
        robot.grab("the stick")
    if check("the stick is positioned behind the thermos and the thermos is not near the target location"):
        robot.push("the thermos towards the goal using the stick")
    if check("the thermos is near the target location"):
        robot.release("the stick and leave the thermos at the goal")