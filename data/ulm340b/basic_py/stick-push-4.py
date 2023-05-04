
    if check("the stick is left of the robot's gripper and the robot's gripper is not vertically aligned with the stick"):
        robot.grab("the stick")
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not around the stick"):
        robot.move("gripper around stick")
    if check("the robot's gripper is below the stick and the stick is below the robot's gripper"):
        robot.push("the thermos to the goal")

# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    if check("the stick is left of the robot's gripper and the robot's gripper is not vertically aligned with the stick"):
        robot.grab("the stick")
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not around the stick"):
        robot.move("gripper around stick")
    if check("the robot's gripper is below the stick and the stick is below the robot's gripper"):
        robot.pull("the thermos to the goal")

# hook-push: grab the hook and use it to push the thermos to the target location
def hook_push(robot):
    if check("the hook is left of the robot's gripper and the robot's gripper is not vertically aligned with the hook"):
        robot.grab("the hook")
    if check("the robot's gripper is vertically aligned with the hook and the robot's gripper is not around the hook"):
        robot.move("gripper around hook")
    if check("the robot's gripper is below the hook and the hook is below the robot's gripper"):
        robot.push("the thermos to the goal")

# hook-pull: grab the hook and use it to pull the thermos to the target location
def hook_pull(robot):
    if check("the hook is left of the robot's gripper and the robot's gripper is not vertically aligned with the hook"):
        robot.grab("the hook")
    if check("the robot's gripper is vertically aligned with the hook and the robot's gripper is not around the hook"):
        robot.move("gripper around hook")
    if check("the robot's gripper is below the hook and the hook is below the robot's gripper"):
        robot