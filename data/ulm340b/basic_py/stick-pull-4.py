
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above the stick")
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not around the stick"):
        robot.put("gripper around the stick")
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is around the stick"):
        robot.grab("stick")
    if check("the robot's gripper is almost vertical and the robot's gripper is around the stick"):
        robot.move("stick to thermos")
    if check("the stick is near the thermos"):
        robot.move("thermos to the goal")

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above the stick")
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not around the stick"):
        robot.put("gripper around the stick")
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is around the stick"):
        robot.grab("stick")
    if check("the robot's gripper is vertical and the robot's gripper is around the stick"):
        robot.move("stick to thermos")
    if check("the stick is near the thermos"):
        robot.move("thermos to the goal")

# stick-tap: grab the stick and use it to knock the thermos off the table
def stick_tap(robot):
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above the stick")
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not around the stick"):
        robot.put("gripper around the stick")
    if check("the robot's gripper is vertical and the robot's gripper is around the stick"):
        robot.grab("stick")
    if check("the robot's gripper is vertical and the robot's gripper is around the stick"):
        robot.move("stick to thermos")
    if check("the stick is near the thermos