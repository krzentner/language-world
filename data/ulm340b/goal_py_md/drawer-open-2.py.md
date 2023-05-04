

The robot can check the positions of objects in two different frames of reference: "above" and "forward aligned".
For example, if the robot's gripper is above the drawer and we call:

```
check("the robot's gripper is not vertically aligned with drawer handle")
```

it returns True.
If the robot's gripper is roughly around the drawer and we call:

```
check("the robot's gripper is forward aligned with the drawer handle")
```

it returns True.

Once you write your solution, feel free to read through our solution:

```
# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Pull the drawer open
    # If the gripper is not near the drawer handle, move it to the drawer handle.
    # We need to be careful about the direction, since it's hard to grab the
    # drawer when it's not lined up with the gripper from in front.
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # pull the drawer open.
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.move_gripper("near the drawer handle", close_gripper=True)
```

Now, try to write a program for a robot without a gripper, for the task `door-open-no-gripper`:

```
# door-open-no-gripper: move the door open
def door_open_no_gripper(robot):
```

Begin by writing a program, and then feel free to compare it with our solution:

```
# door-open-no-gripper: move the door open
def door_open_no_gripper(robot):
    # Steps:
    #  1. Put robot near the door
    #  2. Start moving the door
    #  3. Move the door all the way open
    if check("the robot is not near the door handle"):
        robot.move_robot("near the door handle")
    if check("the robot is not almost vertically aligned with door handle"):
        robot.move_robot("in front of the door handle")
   