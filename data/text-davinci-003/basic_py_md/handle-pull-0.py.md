

Then add the following code to complete the task:

```
    if check("the robot's gripper is not near the door handle"):
        robot.place("gripper near door handle")
    if check("the robot's gripper is not around door handle and the robot's gripper is open"):
        robot.grab("door handle")
    if check("the robot's gripper is around door handle"):
        robot.pull("upwards on door handle")
```