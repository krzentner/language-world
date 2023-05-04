

Then write several `check` conditions to handle the task, followed by `robot` commands.
Use the following as a reference:

```
# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")
```

Note that you may call any of the previously defined functions to solve this task.

When you are finished, click "Submit".

You can check the boxes below to view different functions that can be called.

__functions that move the robot's gripper:__

```
robot.move("gripper to the right of window handle")
robot.move("gripper down to door handle")
robot.grab("drawer handle")
robot.put("gripper above button")
robot.place("gripper above puck")
robot.drop("gripper around puck")
robot.align("peg to hole")
robot.insert("peg into hole")
robot.reach("to goal")
robot.slide("window left")
robot.push("window left harder")
robot.slide("window right")
robot.push("window right harder")
robot.pull("away from drawer")
robot.pull("door open")
robot.push("the gripper into the puck")
robot.slide("the puck to the goal")
```
__functions that open or close the robot's gripper:__

```
robot.close("gripper around puck")
```

__functions that perform actions:__

```
robot.push("down on button")
robot.put("gripper around drawer handle")
robot.push("drawer closed")
robot.put("gripper around peg")
robot.grab("peg")
robot.insert("peg into hole")
robot.place("puck at goal")
```
__functions that check if conditions are met:__

```
if check("the robot's gripper is not vertically aligned with button"):
if check("the robot's gripper is not vertically aligned with drawer handle"):
if check("the robot's gripper is not almost vertically aligned with door handle"):
if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
if check("the robot's gripper is forward aligned with the peg and the peg is