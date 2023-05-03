# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    if check("the robot's gripper is not near the coffee mug handle"):
        robot.put("gripper above coffee mug handle")
    if check("the robot's gripper is near the coffee mug handle and the robot's gripper is open"):
        robot.grab("coffee mug handle")
    if check("the robot's gripper is around the coffee mug handle and the coffee mug is not on the target location"):
        robot.pull("coffee mug to target location")