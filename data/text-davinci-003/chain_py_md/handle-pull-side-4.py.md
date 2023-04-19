

The code for handle-pull-side would look like this:

```
# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper just above handle
    #  2. Grab handle with gripper
    #  3. Pull handle with gripper
    # We need to be careful to line up the gripper with the handle, since the 
    # handle is small and the robot's gripper is round.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper just above handle")
    # Once the gripper is lined up above the handle, grab the handle by moving 
    # the gripper down around it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.grab("gripper around handle")
    # Now that the gripper is around the handle, we can just pull the handle up.
    if check("the robot's gripper is around handle"):
        robot.pull("up on handle")
```