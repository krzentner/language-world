

then press **enter** to add a line to your file.
Type the rest of the program to solve the task.

Use the text
```python
if check("CONDITION"):
    robot.move_gripper("ACTION")
```
to check a condition and run an action.
Use the text
```python
and
or
not
```
to make more complex conditions.

You can check if a certain object has a certain property or not with the format
```
"the [OBJECT]'s [PROPERTY]"
```
Objects are:
```
robot's gripper
puck
door handle
drawer handle
button
basketball
hoop
peg
hole
window handle
```
Properties are:
```
closed
open
below
above
right of
left of
near
far
in front of
vertically aligned with
horizontally aligned with
forward aligned with
almost vertically aligned with
```

You can check the position of the gripper with:
```
"the robot's gripper is [POSITION]"
```

You can check the direction of the gripper with:
```
"the robot's gripper is [DIRECTION]"
```

You can check the status of the gripper with:
```
"the robot's gripper is [STATUS]"
```

To move the gripper use
```python
robot.move_gripper("ACTION")
```

You can close the gripper by setting `close_gripper=True`:
```python
robot.move_gripper("ACTION", close_gripper=True)
```

You can use an extra argument `gripper_position`:
```python
robot.move_gripper("ACTION", gripper_position=True)
```

The possible actions are:
```
"right"
"left"
"up"
"down"
"left of [OBJECT]"
"right of [OBJECT]"
"forward of [OBJECT]"
"behind [OBJECT]"
"left of [OBJECT], forward of [OBJECT]"
"right of [OBJECT], forward of [OBJECT]"
"left of [OBJECT], behind [OBJECT]"
"right of [OBJECT], behind [OBJECT]"
"forward of [OBJECT]"
"behind [OBJECT]"
"above [OBJECT]"
"below [OBJECT]"
"vertically aligned with [OBJECT]"
"horizontally aligned with [OBJECT]"
"forward aligned with [OBJECT]"
"almost vertically aligned with [OBJECT]"
"left of [OBJECT], above [OBJECT]"
"right of [OBJECT], above [OBJECT]"
"left of [OBJECT], below [OBJECT]"
"right of [OBJECT], below [OBJECT]"
"above [OBJECT