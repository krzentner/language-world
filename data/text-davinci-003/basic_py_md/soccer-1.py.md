

Here's the code to perform the task:

```
# soccer: push the soccer ball into the target location
# def soccer(robot):
    if check("the robot's gripper is not above the soccer ball"):
        robot.place("gripper above soccer ball")
    if check("the robot's gripper is not around soccer ball and the robot's gripper is open"):
        robot.drop("gripper around soccer ball")
    if check("the robot's gripper is around the soccer ball and the soccer ball is not in range of the goal"):
        robot.push("soccer ball forwards")
    if check("the robot's gripper is around the soccer ball and the soccer ball is in range of the goal"):
        robot.release("soccer ball")
```