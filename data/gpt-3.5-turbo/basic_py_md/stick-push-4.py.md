# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    if check("the stick is not near the thermos"):
        robot.reach("to the stick")
        robot.grab("the stick")
    if check("the robot's gripper is not above the thermos and the stick is not vertical"):
        robot.put("the gripper above the stick and the stick vertically")
    if check("the robot's gripper is not above the thermos and the stick is vertical"):
        robot.put("the gripper above the thermos")
        robot.push("the stick towards the thermos")
    if check("the robot's gripper is above the thermos and the stick is vertical"):
        robot.push("the stick towards the goal")