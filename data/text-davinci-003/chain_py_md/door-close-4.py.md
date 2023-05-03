

Now your code:
```
# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper to the left of the door handle
    #  2. Push against the door handle to close the door
    #  3. Push harder on the door handle to close it
    
    # First, move the gripper to the left of the door handle, so we can push it closed.
    if check("the robot's gripper is not to the left of the door handle and the robot's gripper is below the door handle"):
        robot.put("gripper to the left of the door handle")
    # If the gripper is near the door handle, we can try to push the door closed.  
    if check("the robot's gripper is near the door handle"):
        robot.push("door closed")
    # If the gripper is still in front of the door handle, we need to push harder to close the door.
    if check("the robot's gripper is in front of the door handle"):
        robot.push("door closed harder")
```