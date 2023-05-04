

Here are some of the conditions you can use:

```
check("the robot's gripper is left of the door knob")
check("the robot's gripper is in front of the door knob")
check("the door knob is open")
check("the door knob is open and the door knob is vertically aligned with the door")
check("the door knob is not open")
check("the robot's gripper is above the door knob")
check("the door knob is vertically aligned with the door")
check("the door knob is not vertically aligned with the door")
```

And some actions:

```
robot.close("gripper around door knob")
robot.grab("door knob")
robot.move("gripper to left of door knob")
robot.move("gripper to right of door knob")
robot.turn("door knob to the right")
robot.turn("door knob to the left")
robot.release("gripper from door knob")
```

Please remember that you cannot open the door knob before it's in the correct position.



```
# door-lock: turn the dial on the door
def door_lock(robot):
    if check("the robot's gripper is not above the door knob"):
        robot.put("gripper above door knob")
    if check("the door knob is open"):
        robot.close("gripper around door knob")
    if check("the robot's gripper is closed around door knob and the door knob is not vertically aligned with door"):
        robot.release("gripper from door knob")
    if check("the robot's gripper is almost vertically aligned with the door knob"):
        robot.turn("door knob to the right")
    if check("the robot's gripper is in front of the door knob"):
        robot.release("gripper from door knob")
```
)

gen_description(
"""
### Door Unlock

Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

Here's some code that demonstrates how the robot can do a variety of tasks:

```
# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# reach: reach to the target location
def reach(robot):
 