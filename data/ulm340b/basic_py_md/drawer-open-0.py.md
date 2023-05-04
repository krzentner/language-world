

and then write code that will pass the test cases below.
Note that all other tasks have already been correctly implemented, so you can rely on them to do the subtasks that are in their names.

Test case 1:

```
def window_open(robot):
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")

def drawer_open(robot):
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.move("gripper above drawer handle")
    if check("the robot's gripper is almost vertically aligned with drawer handle and the robot's gripper is open"):
        robot.move("gripper around drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.pull("drawer open")

# window-open: slide the window open to the left
window_open(robot)

# drawer-open: pull the drawer open
drawer_open(robot)
```

Test case 2:

```
def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

def drawer_open(robot):
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is almost vertically aligned with drawer handle and the robot's gripper is open"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.pull("drawer open")

# drawer-close: push the drawer close
drawer_close(robot)

# drawer-open: pull the drawer open
drawer_open(robot)
```

If your code can handle these test cases, and it is elegant, then you are done. You can try your code on the real robot at this [link](https://robot