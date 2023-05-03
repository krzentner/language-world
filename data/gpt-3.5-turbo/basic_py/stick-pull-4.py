# move-stick: move the stick to the thermos
def move_stick(robot):
    if check("the robot's gripper is not near the stick"):
        robot.reach("for the stick")
    if check("the robot's gripper is near the stick and the robot's gripper is not around the stick"):
        robot.grab("the stick")
    if check("the robot's gripper is around the stick and the stick is not aligned with the thermos"):
        robot.move("the stick to the thermos")

# pull-thermos: pull the thermos using the stick
def pull_thermos(robot):
    if check("the robot's gripper is not almost vertically aligned with the thermos handle"):
        robot.put("gripper above thermos handle")
        robot.put("stick behind thermos handle")
    if check("the stick is behind the thermos handle and the robot's gripper is almost vertically aligned with the thermos handle"):
        robot.pull("thermos using the stick")

# release-stick: release the stick at the target location
def release_stick(robot):
    if check("the robot's gripper is not near the goal location"):
        robot.reach("for the goal location")
    if check("the robot's gripper is near the goal location and the stick is held by the gripper"):
        robot.drop("the stick at the goal location")