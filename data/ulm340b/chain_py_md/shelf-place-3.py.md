

# Dialogue

We have 465 dialogues in total. Please enter the code that makes the robot perform the task. You can run `python test.py --dialogue --task <name>` to check if the code performs the task well.

```
Robot>
```

## Examples

- Please enter the code to have the robot perform the task "button-press-topdown":

```
Robot> # button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
Robot> 
```

- Please enter the code to have the robot perform the task "drawer-open":

```
Robot> # drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is open"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is vertically aligned with the drawer handle"):
        robot.pull("drawer open")
Robot> 
```

- Please enter the code to have the robot perform the task "drawer-close":

```
Robot> # drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")
Robot> 
```

- Please enter the code to have the robot perform the task "door-open":

```
Robot> # door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open