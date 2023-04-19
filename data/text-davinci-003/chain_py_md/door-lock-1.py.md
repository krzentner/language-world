

The steps for this task are as follows:
1. Put the gripper above the door lock
2. Drop the gripper around the door lock
3. Turn the door lock with the gripper

```
# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put gripper above door lock
    #  2. Drop gripper around door lock
    #  3. Turn the door lock with the gripper 
    if check("the robot's gripper is not above the door lock"):
        robot.put("gripper above door lock")
    # As long as the gripper is above, but not around the door lock, put it around the door lock
    if check("the robot's gripper is above the door lock and the robot's gripper is not around the door lock"): 
        robot.drop("gripper around door lock")
    # If the gripper is around the door lock, try to turn it with the gripper
    if check("the robot's gripper is around the door lock"):
        robot.turn("door lock clockwise with gripper")
```