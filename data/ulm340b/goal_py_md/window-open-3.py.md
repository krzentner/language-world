

Use the `move_gripper` method to move the robot's gripper into different
configurations.

The method `move_gripper` takes two parameters, a string that determines how
to move the robot's gripper and a boolean that determines whether to close the
robot's gripper.

The allowed strings are:

- `"forward aligned with ..."`: move the gripper so that it is almost in front
  of an object as viewed from above
- `"left of ..."`: move the gripper so that it is mostly left of an object as
  viewed from above
- `"near ..."`: move the gripper near an object
- `"above ..."`: move the gripper so that it is almost above an object as
  viewed from above
- `"around ..."`: move the gripper so that it is around an object
- `"vertically aligned with ..."`: move the gripper so that it is vertically
  aligned with an object as viewed from the side
- `"around ..."`: move the gripper so that it is around an object
- `"below ..."`: move the gripper so that it is below an object as viewed from
  the side
- `"horizontally aligned with ..."`: move the gripper so that it is horizontally
  aligned with an object as viewed from the side

```
robot.move_gripper("forward aligned with reach target", True)
```

```
robot.move_gripper("left of reach target", False)
```

```
robot.move_gripper("near reach target", False)
```

```
robot.move_gripper("above reach target", False)
```

```
robot.move_gripper("around reach target", False)
```

```
robot.move_gripper("vertically aligned with reach target", False)
```

```
robot.move_gripper("below reach target", False)
```

```
robot.move_gripper("horizontally aligned with reach target", False)
```

The objects allowed are:

- `"reach target"`: the target
- `"the button"`: the button
- `"button"`: the button
- `"the puck"`: the puck
- `"puck"`: the puck
- `"the peg"`: the peg
- `"peg"`: the peg
- `"the drawer handle"`: the drawer handle
- `"drawer handle"`: the drawer handle
- `"the window handle"`: the window handle
- `"window handle"`: the window handle
- `"the door handle"`: the door handle
- `