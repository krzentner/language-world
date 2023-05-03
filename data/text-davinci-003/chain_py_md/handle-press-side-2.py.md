

Here's the answers:

```
# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:    
    #  1. Put gripper close to handle from the side
    #  2. Push down on handle
    #  3. Hold handle down
    # First, put the gripper close to the handle from the side.
    if check("the robot's gripper is not close to the handle with it's side"):
        robot.move("gripper close to handle from the side")
    # If the gripper is close to the handle and not pressed down yet, start
    # pushing the handle down.
    if check("the robot's gripper is close to the handle with it's side and the handle is not pushed down"):
        robot.push("down on handle")
    # Once the handle is pressed down, hold it down.
    if check("the handle is pushed down"):
        robot.hold("handle down")
```