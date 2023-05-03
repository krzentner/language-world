

Then, our program can look like this: 

```
# handle-press: push down the handle
# def handle_press(robot):
    # Steps:
    #  1. Put the gripper above the handle
    #  2. Drop down the gripper around the handle
    #  3. Push down on the handle
    # First, put the gripper roughly above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # We can see the handle from above, so if the gripper is near it but not
    # around it, drop the gripper around it.
    if check("the robot's gripper is not around the handle and the robot's gripper is near the handle"):
        robot.drop("gripper around handle")
    # Once the gripper is around the handle, we can just push down on the
    # handle.
    if check("the robot's gripper is around handle"):
        robot.push("down on handle")
```