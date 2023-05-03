# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    if check("the robot's gripper doesn't hold the stick"):
        robot.grab("the stick")
    if check("the robot's gripper is not above the thermos and the stick is not pointing towards the thermos"):
        robot.rotate("the stick towards the thermos")
    if check("the stick is pointing towards the thermos and the robot's gripper is not above the thermos"):
        robot.move("the gripper above the thermos")
    if check("the robot's gripper is above the thermos and the stick is pointing at the thermos"):
        robot.push("the stick towards the target")
    if check("the thermos has reached the target location"):
        robot.drop("the stick")