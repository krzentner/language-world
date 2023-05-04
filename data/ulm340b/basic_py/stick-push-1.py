
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("stick is not left of the robot's gripper and stick is not forward aligned with the robot's gripper"):
        robot.grab("stick")
    if check("the robot's gripper is forward aligned with the stick and the stick is not aligned with the thermos"):
        robot.align("stick with thermos")
    if check("stick is aligned with thermos"):
        robot.push("thermos to goal")

# stick-hook: grab the stick and use it to pull the thermos to the target location
def stick_hook(robot):
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("stick is not left of the robot's gripper and stick is not forward aligned with the robot's gripper"):
        robot.grab("stick")
    if check("the robot's gripper is forward aligned with the stick and the stick is not aligned with the thermos"):
        robot.align("stick with thermos")
    if check("stick is aligned with thermos"):
        robot.pull("thermos to goal")

# lever-pull: grab the lever and pull it to the target location
def lever_pull(robot):
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.put("gripper above lever")
    if check("lever is not left of the robot's gripper and lever is not forward aligned with the robot's gripper"):
        robot.grab("lever")
    if check("the robot's gripper is forward aligned with the lever and the lever is not aligned with the goal"):
        robot.align("lever with goal")
    if check("lever is aligned with goal"):
        robot.pull("lever to goal")

# hammer-tap: grab the hammer and tap the peg to the target location
def hammer_tap(robot):
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.put("gripper above hammer")
    if check("hammer is not left of the robot's gripper and hammer is not forward aligned with the robot's gripper"):
        robot.grab("hammer")
    if check("the robot's gripper is forward aligned with the hammer and the hammer is