

Then, add the code to complete the task:

```
# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not near the puck"):
        robot.place("gripper near puck")
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.slide("puck to goal")
    if check("the puck is near goal"):
        robot.release("puck at goal")
```