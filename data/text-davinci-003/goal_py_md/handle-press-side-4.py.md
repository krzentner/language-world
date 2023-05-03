

The steps to perform this task are:

1. Put gripper above handle 
2. Drop gripper around handle 
3. Push down on the handle from the side 

The code would look like this:

```
# handle-press-side: push down the handle from the side 
def handle_press_side(robot):

    # Put gripper above handle 
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle ")

    # Drop gripper around handle 
    if check("the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle", close_gripper=True)

    # Push down on the handle from the side 
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("side of the handle")
```