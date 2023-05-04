

It might help to know that the goal of the task is the dial, and the robot is looking left in front of it.

Note that you can also use the following code to test if the robot's gripper is in the direction of the door.

```
# Test if the robot's gripper is vertically aligned with the door handle
print(check("the robot's gripper is vertically aligned with door handle"))
# Test if the robot's gripper is not vertically aligned with the door handle
print(check("the robot's gripper is not vertically aligned with door handle"))
```
"""
# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # As long as the gripper is lined up, closing it should grab the dial.
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    # As long as the gripper is still around the dial, it's being turning, so keep pulling.
    if check("the robot's gripper is around door handle"):
        robot.pull("dial")

"""

Please now use the following prompt to generate the code for the rest of the tasks:

```
# Task:
def <task_name>(robot):
    # Steps:
    #  1. 
    #  2. 
    #  3. 
    #  4. 
    #  5. 
    # If the <condition>
    if check("<task_name> <condition>"):
        robot.<verb>("<noun>")
```

For example, to get the robot to perform the task `drawer-close`, you could start with the prompt:

```
# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed
    # If the gripper