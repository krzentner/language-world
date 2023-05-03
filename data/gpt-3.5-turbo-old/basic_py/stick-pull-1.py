if check("the stick is not in the robot's gripper"):
        robot.grab("the stick")
    if check("the stick is not touching the thermos"):
        robot.slide("the stick to touch the thermos")
    if check("the stick is touching the thermos and the thermos is not at the goal location"):
        robot.pull("the thermos to the goal")
    if check("the thermos is at the goal location"):
        robot.release("the stick")