

Please describe what you would like the program to do:

```
# Steps:
#  1. Put gripper above the handle
#  2. Drop the gripper onto the handle
#  3. pull the handle up
#  4. pull the handle out
```

Write code below to implement the above steps. You will need to insert the
lines above at the right spots.

```
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.place("the robot's gripper above the handle")
    # Once the gripper is above the handle, put it around the handle.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around the handle"):
        robot.place("the robot's gripper around the handle")
    # Once the gripper is around the handle, pull the handle up.
    if check("the robot's gripper is around the handle"):
        robot.pull("up on the handle")
    # Once the handle is pulled up, pull the handle out.
    if check("the robot's gripper is around the handle and the handle is out"):
        robot.pull("the handle out")
```

Good work!
Now, for the final exercise, please complete the following task:

```
# door-pull: pull the door open
def door_pull(robot):
```

Please write down the steps required:

```
    # Steps:
    #  1. Put gripper above the door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
```

Write code below to implement the above steps.

```
    # First, put the gripper above the door handle.
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.place("the robot's gripper above the door handle")
    # Once the gripper is above the door handle, put it around the door handle.
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not around the door handle"):
        robot.place("the robot's gripper around the door handle")
    # Once the gripper is around the door handle, pull open the door.
    if check("the robot'