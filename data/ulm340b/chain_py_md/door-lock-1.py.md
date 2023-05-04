


The task is to use the robot's gripper to *turn the dial on the door*. The steps are to:

1. Put the robot's gripper around the dial on the door.
2. Move the gripper sideways to turn the dial.

Here is how the robot can do this task:

```
# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put the robot's gripper around the dial on the door.
    #  2. Move the gripper sideways to turn the dial.
    # We need to start with the robot's gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.put("the robot's gripper around the dial")
    # As long as the gripper is around the dial, move it sideways to turn the
    # dial.
    if check("the robot's gripper is around the dial"):
        robot.move("gripper sideways")
```

'''


def door_lock(robot):
    # door-lock: turn the dial on the door
    # Steps:
    #  1. Put the robot's gripper around the dial on the door.
    #  2. Move the gripper sideways to turn the dial.
    # We need to start with the robot's gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.put("the robot's gripper around the dial")
    # As long as the gripper is around the dial, move it sideways to turn the
    # dial.
    if check("the robot's gripper is around the dial"):
        robot.move("gripper sideways")

# window-open: slide the window open to the left
def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper near the window handle to start pushing
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below