# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    if check("the robot's gripper is not holding the stick and the robot's gripper is not near the stick"):
        robot.pick("the stick")
    if check("the robot's gripper is holding the stick and the stick is not near the thermos"):
        robot.move("the stick to the thermos")
    if check("the robot's gripper is holding the stick and the stick is near the thermos"):
        robot.push("the thermos to the goal location using the stick")