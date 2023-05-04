

The code should perform the following steps:

- Steps:
-  1. Line up the gripper from above, to the left of the lock
-  2. Grab and push down on the lock
-  3. Turn the lock counterclockwise
-  4. Line up the lock with the dial, a little off
-  5. Insert the lock into the dial
-  6. Turn the dial counter-clockwise
-
- To line up from above, we should also check if the lock is left of the gripper.
- Since the lock is round, we can insert it into the dial from the side.

Note that your code must not include an "else". If your code passes the first 14
tasks, but fails on the 15th, check to make sure you've removed any "else"
statements.

The `door-unlock` task will fail the first time you submit your code because it
is missing the line:

```
# door-unlock: turn the dial on the door
def door_unlock(robot):
    # To line up from above, we should also check if the lock is left of the gripper.
    # Since the lock is round, we can insert it into the dial from the side.
```

You can fill in this line and it will pass when you submit it again.

If you get stuck, you can ask me for help by writing "hint()".

"""
    print("Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.")
    print("Here's some code that demonstrates how the robot can do a variety of tasks:")

    print("""# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pushing it (unlike when opening the drawer).
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # push the drawer closed.
    if check("the robot's gripper is forward aligned