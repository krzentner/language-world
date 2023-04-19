

Then, add the code to the function:

```
# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull the handle up
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # If the handle is left of the gripper, we should grab it by moving the
    # gripper to the handle.
    if check("handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    # As long as the handle is still forward aligned with the gripper, pull the
    # handle up.
    if check("the robot's gripper is forward aligned with the handle"):
        robot.pull("handle up")
```