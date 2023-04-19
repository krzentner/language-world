

The Steps to complete this task are:
1. Put gripper near door handle
2. Push the door closed

Step 1: Put gripper near door handle
```
    # If the robot's gripper is not near the door handle, move it to the door
    # handle. We don't need to be sure it's perfectly lined up in order to 
    # close the door, so we can just get it near the handle.
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
```

Step 2: Push the door closed
```
    # Once the gripper is near the door handle, start pushing against it to 
    # close the door.
    if check("the robot's gripper is near the door handle"):
        robot.push("door closed")
```

All the code together should look like this:
```
# door-close: push the door closed to the target location
# def door_close(robot):
    # If the robot's gripper is not near the door handle, move it to the door
    # handle. We don't need to be sure it's perfectly lined up in order to 
    # close the door, so we can just get it near the handle.
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    # Once the gripper is near the door handle, start pushing against it to 
    # close the door.
    if check("the robot's gripper is near the door handle"):
        robot.push("door closed")
```