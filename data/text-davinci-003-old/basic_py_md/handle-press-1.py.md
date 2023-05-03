

Next we will check if the robot's gripper is not vertically aligned with the handle: 
```
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
```
Then, we will check if the gripper is vertically aligned with the handle:
```
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.push("down on handle")
```
Finally, we will end the block of code:
```
    return
```