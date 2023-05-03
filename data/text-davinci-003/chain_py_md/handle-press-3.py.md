

and add the following code:

```
    # Steps:
    #  1. Put gripper above the handle
    #  2. Move gripper around the handle
    #  3. Push down on the handle
    # We need to put the gripper above the handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # Once the gripper is lined up above the handle, rotate it around the handle
    # so that it can grab it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.drop("gripper around handle")
    # Once the gripper is around the handle, simply push down on the handle to
    # activate it.
    if check("the robot's gripper is around handle"):
        robot.push("down on handle")
```