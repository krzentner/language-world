

Then we can implement the program like this:

```
# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Push the handle down
    # First, put the gripper above the handle so we don't bump the handle
    # while trying to grab it.
    if check("the robot's gripper is not above handle and the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # Once the gripper is lined up above the handle, we should be able to grab
    # the handle and push it down.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not near handle"):
        robot.put("gripper near handle")
    # Once the gripper is around the handle, push down on the handle.
    if check("the robot's gripper is near handle"):
        robot.push("handle down")
```