
    if check("the robot's gripper is not above the stick and the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("stick is above the robot's gripper and the robot's gripper is not around the stick"):
        robot.grab("stick")
    if check("the robot's gripper is above the stick and the stick is forward aligned with the robot's gripper"):
        robot.slide("stick into thermos")
    if check("the stick is almost near the thermos and the thermos is vertically aligned with the stick and the robot's gripper is above the thermos"):
        robot.push("thermos to goal")

# stick-push-side: grab the stick and use it to push the puck to the target location from the side
def stick_push_side(robot):
    if check("the robot's gripper is not above the stick and the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("stick is above the robot's gripper and the robot's gripper is not around the stick"):
        robot.grab("stick")
    if check("the robot's gripper is above the stick and the stick is forward aligned with the robot's gripper"):
        robot.slide("stick into puck")
    if check("the stick is almost near the puck and the puck is vertically aligned with the stick"):
        robot.push("puck to goal")

# Stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    if check("the robot's gripper is not above the stick and the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("stick is above the robot's gripper and the robot's gripper is not around the stick"):
        robot.grab("stick")
    if check("the robot's gripper is above the stick and the stick is forward aligned with the robot's gripper"):
        robot.slide("stick into thermos")
    if check("the stick is near the thermos and the robot's gripper is forward aligned with the thermos"):
        robot.pull("thermos to goal")

# Stick-pull-side: grab the stick and use it to pull the puck to the target location from the side
def stick_