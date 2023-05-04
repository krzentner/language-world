

Then complete the function `door_close`. This function will move the gripper in ways that are necessary to complete the task.
You should not use the command `robot.slide` to push the door, but instead use other commands, such as `robot.push`.



[See an example of the tasks](https://storage.googleapis.com/robot-learning/public/tasks.html)

---

### Possible solutions
```
# door-close: push the door closed to the target location
def door_close(robot):
    if check("the robot's gripper is not above door handle"):
        robot.place("gripper above door handle")
    if check("the robot's gripper is above door handle and the robot's gripper is not around door handle"):
        robot.place("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.push("the gripper to close the door")
```

```
# door-close: push the door closed to the target location
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is above door handle and the robot's gripper is not near door handle"):
        robot.grab("the door handle")
    if check("the robot's gripper is near door handle"):
        robot.push("the door handle")
```

```
# door-close: push the door closed to the target location
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.pull("door closed")
```

```
# door-close: push the door closed to the target location
def door_close(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is above door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.push("door closed")
```

```
# door-close: push