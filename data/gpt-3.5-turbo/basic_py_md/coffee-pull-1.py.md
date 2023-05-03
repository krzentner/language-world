# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is vertically aligned with the mug and the robot's gripper is not around the mug"):
        robot.put("gripper around mug")
    if check("the robot's gripper is around mug and the robot's gripper is not near coffee machine handle"):
        robot.pull("mug to coffee machine handle")
    if check("the robot's gripper is near coffee machine handle and the coffee machine handle is up"):
        robot.push("coffee machine handle down")
    if check("the robot's gripper is near coffee machine handle and the coffee machine handle is down"):
        robot.pull("mug away from coffee machine")