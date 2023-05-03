# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        robot.lift("mug")
    if check("the robot's gripper is not near the target location"):
        robot.move("gripper to target location")
    if check("the robot's gripper is near the target location"):
        robot.put("the mug at the target location")