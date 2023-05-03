# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not around stick"):
        robot.grab("stick")
    if check("the robot's gripper is around stick and the stick is not touching the thermos"):
        robot.push("stick towards thermos")
    if check("the stick is touching the thermos"):
        if check("the robot's gripper is not vertically aligned with the thermos"):
            robot.put("gripper above thermos")
        if check("the robot's gripper is vertically aligned with the thermos and the robot's gripper is not around thermos"):
            robot.grab("thermos")
        if check("the robot's gripper is around thermos"):
            robot.pull("thermos towards goal")