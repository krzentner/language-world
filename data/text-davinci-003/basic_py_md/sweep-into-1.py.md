

Answer:
```
# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    if check("the robot's gripper is not above the cube and the robot's gripper is not near the cube"):
        robot.put("gripper above the cube")
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.grab("cube")
    if check("the robot's gripper is not above the target and the robot's gripper is closed"):
        robot.move("gripper above the target")
    if check("the robot's gripper is above the target and the robot's gripper is closed"):
        robot.place("cube at goal")
```