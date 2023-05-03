# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above the mug")
    if check("the robot's gripper is vertically aligned with the mug and the robot's gripper is not around the mug"):
        robot.grab("the mug")
    if check("the robot's gripper is around the mug and the robot's gripper is not near the target location"):
        robot.move("gripper to target location")
    if check("the robot's gripper is near the target location and the mug is below the robot's gripper"):
        robot.slide("the mug to the target location")