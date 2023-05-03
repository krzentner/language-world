# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("the robot's gripper is vertically aligned with the stick and the stick is not grabbed"):
        robot.grab("stick")
    if check("the robot's gripper is near the thermos and the stick is grabbed"):
        robot.slide("stick towards thermos")
    if check("the robot's gripper is attached to the thermos by the stick and the thermos is not at the target location"):
        robot.pull("thermos towards goal")