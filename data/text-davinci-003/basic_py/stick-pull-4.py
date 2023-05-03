
    if check("the robot's gripper is not near the stick"):
        robot.reach("to stick")
    if check("the robot's gripper is not around the stick"):
        robot.grab("stick")
    if check("the robot's gripper is around the stick"):
        robot.pull("the thermos to the goal")

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    if check("the robot's gripper is not near the stick"):
        robot.reach("to stick")
    if check("the robot's gripper is not around the stick"):
        robot.grab("stick")
    if check("the robot's gripper is around the stick"):
        robot.push("the thermos to the goal")
        
# stir-spoon: grab the spoon and use it to stir the mixture
def stir_spoon(robot):
    if check("the robot's gripper is not near the spoon"):
        robot.reach("to spoon")
    if check("the robot's gripper is not around the spoon"):
        robot.grab("spoon")
    if check("the robot's gripper is around the spoon"):
        robot.stir("mixture")