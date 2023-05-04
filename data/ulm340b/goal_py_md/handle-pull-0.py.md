

You should write the body of this function.
Use check statements like these:

```
# If we want the gripper to be aligned in a certain direction as seen from
# above, we should include that.
if check("the robot's gripper is not vertically aligned with drawer handle"):
    robot.move_gripper("vertically aligned with the drawer handle")

# If we want the gripper to be aligned in a certain direction as seen from
# the front, we should include that.
if check("the robot's gripper is not forward aligned with drawer handle"):
    robot.move_gripper("forward aligned with the drawer handle")
```

If you need the gripper to be in a certain location, you should specify it,
like this:

```
# If we want the gripper to be above or below an object, we should include
# that.
if check("the robot's gripper is not above drawer handle"):
    robot.move_gripper("above the drawer handle")

# If we want the gripper to be right or left of an object, we should include
# that.
if check("the robot's gripper is not left of drawer handle"):
    robot.move_gripper("left of the drawer handle")
```

If you want the gripper to be near an object, you should specify that, like
this:

```
# If we want the gripper to be around the object, we should specify that the
# gripper should be near it and around it.
if check("the robot's gripper is not near drawer handle and the robot's gripper is not around drawer handle"):
    robot.move_gripper("near the drawer handle and around drawer handle")
```

If you want the gripper to grab an object, you can either do it in two steps
with:

```
# If we want to move the gripper near an object and then close it, we can do it
# in two steps:
if check("the robot's gripper is not near drawer handle and the robot's gripper is not around drawer handle"):
    robot.move_gripper("near drawer handle")
if check("the robot's gripper is near drawer handle and the robot's gripper is open"):
    robot.move_gripper("around drawer handle", close_gripper=True)
```

Or do it in one step with:

```
# If we want to move the gripper near an object and then close it, we can do it
# in two steps:
if check("