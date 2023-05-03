# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not around the middle of the stick"):
        robot.put("gripper around the middle of the stick")
    if check("the robot's gripper is holding the stick and the robot's gripper is not vertically aligned with the thermos"):
        robot.move("the stick to the thermos")
    if check("the robot's gripper is vertically aligned with the thermos and the robot's gripper is not touching the thermos"):
        robot.put("the stick against the thermos")
    if check("the stick is touching the thermos"):
        robot.push("the thermos to the goal")