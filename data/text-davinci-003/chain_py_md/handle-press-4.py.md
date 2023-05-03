

Then finish your program with the following code:

```
    # Steps:
    #  1. Put the gripper above handle
    #  2. Line up the gripper with the handle
    #  3. Push the handle down
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # If the handle is left of the gripper, move the gripper to the handle
    # again.
    # Because the handle is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("handle is not left of gripper and gripper is not forward aligned with handle"):
        robot.grab("handle")
    # To line up the gripper with the handle, move it down.
    if check("the robot's gripper is forward aligned with handle and the robot's gripper is not near handle"):
        robot.align("gripper to handle")
    # If the gripper is near the handle, we can push the handle down.
    # Close the gripper to make sure we keep control of the handle.
    if check("the robot's gripper is near the handle and the handle is below the robot's gripper"):
        robot.push("handle down")
```