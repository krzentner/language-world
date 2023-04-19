# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    if check("the end of the stick is not near the thermos and the robot's gripper is not gripping the stick"):
        robot.grab("stick")
        robot.move("stick to thermos")
    if check("the end of the stick is near the thermos and the robot's gripper is not gripping the thermos"):
        robot.grab("stick and thermos")
    if check("the end of the stick is near the target location"):
        robot.move("stick to the target location")
    if check("the end of the stick is at the target location"):
        robot.push("the thermos to the target location")
    if check("the thermos is at the target location"):
        robot.drop("the thermos")
        robot.drop("the stick")