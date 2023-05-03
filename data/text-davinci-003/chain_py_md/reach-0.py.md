

The robot needs to reach an object in one of two ways: 
1. Lift the gripper to a targeted height, or 
2. Move the gripper to a targeted location. 

First, check to see if the gripper is already at the targeted location or height. 

```
# reach: reach to the target location
def reach(robot):
    # Check to see if the gripper is already at the targeted location or height.
    if check("the robot's gripper is already at the targeted location or height"):
        return # exit out of the function if gripper is already in target position

```

Otherwise, if the gripper is not already at the targeted location, the robot needs to move the gripper to the target position. 

To lift the gripper to the targeted height, we will need to move the gripper up until the gripper reaches the target height. 

```
# reach: reach to the target location
def reach(robot):
    # Check to see if the gripper is already at the targeted location or height.
    if check("the robot's gripper is already at the targeted location or height"):
        return # exit out of the function if gripper is already in target position

    # Move the gripper up until the gripper reaches the target height.
    if check("the robot's gripper is not at the targeted height"):
        robot.lift("gripper to target height")
```

Now, the robot needs to move the gripper to the target location. To do this, we will move the gripper at a fixed speed until the gripper is at the target location. 

```
# reach: reach to the target location
def reach(robot):
    # Check to see if the gripper is already at the targeted location or height.
    if check("the robot's gripper is already at the targeted location or height"):
        return # exit out of the function if gripper is already in target position

    # Move the gripper up until the gripper reaches the target height.
    if check("the robot's gripper is not at the targeted height"):
        robot.lift("gripper to target height")
    
    # Move the gripper at a fixed speed until the gripper is at the target location.
    if check("the robot's gripper is not at the target location"):
        robot.move("gripper to target location at a fixed speed")
```