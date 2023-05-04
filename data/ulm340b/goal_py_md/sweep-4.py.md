

The task can be broken down into the following steps:

  1. Put the robot's gripper above the cube.
  2. Grab the cube with the gripper.
  3. Move the robot's gripper towards the target location.

If the robot's gripper is not above the cube, move the gripper to be above the cube, using the expression:

```
robot.move_gripper("above the cube")
```

If the robot's gripper is above the cube but it is not around the cube, grab the cube using the expression:

```
robot.move_gripper("around the cube", close_gripper=True)
```

If the gripper is around the cube, move the robot's gripper to the target location using the expression:

```
robot.move_gripper("at the target location")
```

As with the other tasks, include comments to describe what's happening.
"""

# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    # Steps:
    #  1. Put the robot's gripper above the cube.
    #  2. Grab the cube with the gripper.
    #  3. Move the robot's gripper towards the target location.

    # Put the gripper above the cube
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")

    # Put gripper around the cube
    if check("the robot's gripper is above the cube and the robot's gripper is not around the cube"):
        robot.move_gripper("around the cube", close_gripper=True)

    # move the robot's gripper to the target location
    if check("the gripper is around the cube"):
        robot.move_gripper("at the target location")

# Run this to verify that your sweep program works.
def main():
    robot = create_robot()
    task = "sweep"
    if task == "button-press-topdown":
        button_press_topdown(robot)
    elif task == "drawer-open":
        drawer_open(robot)
    elif task == "drawer-close":
        drawer_close(robot)
    elif task == "door-open":
        door_open(robot)
    elif task == "window-close":
        window_close(robot)
    elif task