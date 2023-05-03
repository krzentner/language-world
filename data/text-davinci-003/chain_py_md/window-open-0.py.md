

Then continue with the code:

```
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # First, if the window handle is left of the robot's gripper, move the
    # gripper near the window handle to start pushing.
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    # If the robot's gripper is near the window handle, we can probably slide the
    # window open now by moving the gripper left.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder. 
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")    
```