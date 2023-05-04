

Then write a set of condition and action statements to tell the robot to close the door.

For example, you could complete the task `door-close` like this:

```
# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Push the door closed
    # First, put the gripper above the door handle.
    if check("the robot's gripper is not above door handle"):
        robot.put("gripper above door handle")
    # As long as the gripper is above the door handle, closing it should line it up
    # all the way.
    if check("the robot's gripper is above the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    # As long as the gripper is still around the door handle,
    # the door can still be pushed closed
    if check("the robot's gripper is near door handle and the robot's gripper is around door handle"):
        robot.push("door closed")
```

We can see that the above program performs the task `door-close` correctly:

```
> run task door-close
robot.put("gripper above door handle")
robot.put("gripper around door handle")
robot.push("door closed")
```

Please write a program to perform the task `door-close`. 
"""

task_name = 'door-close'

def door_close(robot):
    # Steps:
    #  1. Put gripper roughly above the door handle
    #  2. Drop gripper around door handle
    #  3. Push the door closed

    if check("the robot's gripper is not above the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is above the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is near door handle and the robot's gripper is around door handle"):
        robot.push("door closed")


print("""
<h3>Congratulations!</h3>
You've completed a task on a robot using