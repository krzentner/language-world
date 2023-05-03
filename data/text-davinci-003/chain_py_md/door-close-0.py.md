

Steps:  
1. Put gripper above the door handle  
2. Drop gripper around the door handle  
3. Push the door closed  

```
# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Push the door closed
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    # As long as the gripper is still vertically aligned with the door handle,
    # it's being opened, so keep pushing.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.push("door closed")
```