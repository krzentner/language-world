

Then, write the actual code to perform the task:

```
# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not near the puck"):
        robot.reach("to puck")
    if check("the robot's gripper is near the puck and the robot's gripper is not around the puck"):
        robot.grab("puck")
    if check("the robot's gripper is around the puck and the puck is not forward aligned with the robot's gripper"):
        robot.align("puck in front of gripper")
    if check("the puck is forward aligned with the robot's gripper and the puck is not horizontally aligned with the goal"):
        robot.slide("puck towards goal")
    if check("the puck is horizontally aligned with the goal"):
        robot.push("puck into goal")
```