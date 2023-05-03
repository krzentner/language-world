# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    if check("the robot's gripper is not vertically aligned with the handle of the mug"):
         robot.put("gripper above mug handle")
    if check("the robot's gripper is vertically aligned with the handle of the mug and the robot's gripper is open"):
        robot.put("gripper around mug handle")
    if check("the robot's gripper is around mug handle"):
        robot.pull("mug to goal")