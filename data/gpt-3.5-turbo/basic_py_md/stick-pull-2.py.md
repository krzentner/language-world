# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("the stick is not in the robot's gripper"):
        robot.grab("stick")
    if check("the robot's gripper is not aligned horizontally with the thermos handle"):
        robot.move("gripper to the right of the thermos")
    if check("the robot's gripper is aligned horizontally with the thermos handle"):
        robot.put("gripper around the thermos handle")
    if check("the robot's gripper is around the thermos handle"):
        robot.pull("thermos to the target location")