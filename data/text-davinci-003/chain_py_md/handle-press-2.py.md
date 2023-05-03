

Then add your code:

```
# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Push down on handle
    # First, we need to put the gripper above the handle so we can line it up.
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    # If the gripper is more than almost vertically aligned with the handle, drop
    # it around the handle.
    if check("the robot's gripper is not almost vertically aligned with the handle"):
        robot.drop("gripper around handle")
    # Once the gripper is around the handle, close the gripper to make a good
    # seal and push down.
    if check("the robot's gripper is almost vertically aligned with the handle and the robot's gripper is open"):
        robot.close("gripper around handle")
        robot.push("down on handle")
```