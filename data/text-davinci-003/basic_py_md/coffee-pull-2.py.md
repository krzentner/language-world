

Answer:
```
# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.grab("mug handle")
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug handle")
    if check("the robot's gripper is around mug handle and the robot's gripper is closed"):
        robot.pull("mug to goal")
``