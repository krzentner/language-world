

Next, add the following code:

```
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.pull("drawer open")
```

Finally, close the function with:
    
```
    robot.init()
```