

You will also need to refer to the object `robot`, which gives you information
about the locations of objects and allows you to move the robot's gripper.

Use the following functions of `robot`:
- `robot.move_gripper(where)`: moves the gripper to the specified location
- `robot.gripper_location()`: where the gripper is right now
- `robot.gripper_direction()`: the direction the gripper is facing right now
- `robot.gripper_is_open()`: whether the gripper is open
- `robot.gripper_is_closed()`: whether the gripper is closed

You can also call the following functions to check if a proposition about the
world state is true. For example,
```
if check("the puck is near the handle"):
    robot.move_gripper("near the handle")
```

You can check the following propositions:
- `"the robot's gripper is open"`
- `"the robot's gripper is closed"`
- `"the robot's gripper is near the reach target"`
- `"the puck is near the reach target"`
- `"the robot's gripper is near the puck"`
- `"the puck is left of the robot's gripper"`
- `"the puck is right of the robot's gripper"`
- `"the puck is below the robot's gripper"`
- `"the robot's gripper is vertically aligned with the puck"`
- `"the robot's gripper is horizontally aligned with the puck"`
- `"the puck is near the target location"`
- `"the puck is on top of the target location"`
- `"the window is open"`
- `"the window is closed"`
- `"the window handle is right of the robot's gripper"`
- `"the window handle is left of the robot's gripper"`
- `"the window handle is in front of the robot's gripper"`
- `"the robot's gripper is vertically aligned with window handle"`
- `"the robot's gripper is horizontally aligned with window handle"`
- `"the window handle is near the robot's gripper"`
- `"the robot's gripper is forward aligned with window handle"`
- `"the robot's gripper is almost vertically aligned with window handle"`
- `"the robot's gripper is vertically aligned with window handle"`
- `"the drawer is open"`
- `"the drawer is closed"`
- `"the drawer handle is vertically aligned with the robot's gripper"`
- `"the drawer handle is