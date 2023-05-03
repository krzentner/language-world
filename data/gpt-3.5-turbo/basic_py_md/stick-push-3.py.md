# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("the stick is not between the robot's gripper and the thermos"):
        robot.grab("stick")
    if check("the robot's gripper is vertically aligned with the stick and the stick is not near the thermos"):
        robot.move("gripper to thermos")
    if check("the robot's gripper is near the thermos and the thermos is below the robot's gripper"):
        robot.push("stick into thermos")
    if check("the thermos is near the goal"):
        robot.push("thermos to goal with stick")