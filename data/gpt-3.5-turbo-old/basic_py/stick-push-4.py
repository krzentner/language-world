if check("the robot's gripper is not holding the stick and the stick is not in contact with the thermos"):
        robot.grab("stick")
    if check("the stick is in contact with the thermos and the thermos is not at the target location"):
        robot.push("thermos towards the target location using the stick")
    if check("the thermos is at the target location"):
        robot.release("stick")
        robot.place("thermos at the goal location")