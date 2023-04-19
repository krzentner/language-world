

The program should read as follows:

```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper near the handle
    #  2. Push down the handle
    # 
    # First, move the gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.put("gripper near handle")
    # Once the gripper is near the handle, push it down.
    if check("the robot's gripper is near the handle"):
        robot.push("down on handle")
```