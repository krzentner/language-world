

Answer:
```
# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not near the puck"):
        robot.move("gripper near puck")
    if check("the robot's gripper is near the puck"):
        robot.grab("puck")
    if check("the robot's gripper is holding the puck"):
        robot.slide("puck to goal")
    if check("the puck is at the goal location"):
        robot.release("puck at goal location")
```