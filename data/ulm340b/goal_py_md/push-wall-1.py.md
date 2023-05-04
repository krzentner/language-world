

To begin, let's go over what you need to do in `push-wall`.

- Step 1: move the robot's gripper near the puck
- Step 2: move the robot's gripper to the top of the puck
- Step 3: push the puck along the wall
- Step 4: move the robot's gripper to the other side of the puck
- Step 5: move the robot's gripper to the top of the puck
- Step 6: slide the puck to the target location

We'll get you started.

`check()` can test whether the robot is in certain positions or configurations.
As you can see, `check()` calls return booleans indicating whether or not they
are true.

```
# This code returns a boolean saying if the puck is not above the robot's gripper
print(check("the puck is above the robot's gripper"))
# This code returns a boolean saying if the puck is below the robot's gripper
print(check("the puck is below the robot's gripper"))
```

The available `check()` calls are as follows:

```
check("the robot's gripper is near [object]")
check("the robot's gripper is not near [object]")

check("the robot's gripper is above [object]")
check("the robot's gripper is not above [object]")
check("the robot's gripper is vertically aligned with [object]")
check("the robot's gripper is not vertically aligned with [object]")
check("the robot's gripper is almost vertically aligned with [object]")
check("the robot's gripper is left of [object]")
check("the robot's gripper is not left of [object]")
check("the robot's gripper is below [object]")
check("the robot's gripper is not below [object]")
check("the robot's gripper is horizontally aligned with [object]")
check("the robot's gripper is not horizontally aligned with [object]")
check("the robot's gripper is right of [object]")
check("the robot's gripper is not right of [object]")

check("the robot's gripper is behind [object]")
check("the robot's gripper is not behind [object]")
check("the robot's gripper is around [object]")
check("the robot's gripper is not around [object]")
check("the robot's gripper is forward aligned with [object]")
check("the robot's gripper is not forward aligned with [object]")
check("the robot's gripper is in front of [