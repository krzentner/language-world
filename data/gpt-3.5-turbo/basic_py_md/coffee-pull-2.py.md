# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    if check("the robot's gripper is not above the mug"):
        robot.put("the gripper above the mug")
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    if check("the robot's gripper is around mug and the robot's gripper is not vertically aligned with the target location"):
        robot.move("the gripper above the target location")
    if check("the robot's gripper is vertically aligned with the target location"):
        robot.pull("the mug to the target location")