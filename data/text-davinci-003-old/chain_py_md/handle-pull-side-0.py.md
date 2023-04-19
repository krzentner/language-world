

The program should be:

```
# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper to the side of the handle
    #  2. Grab the handle with the gripper
    #  3. Pull the handle up
    # We need to put the gripper to the side of the handle before we can grab it.
    if check("the robot's gripper is not to the side of the handle"):
        robot.put("gripper to side of handle")
    # Once the gripper is lined up to the side of the handle, we should be able to
    # grab the handle by moving the gripper around it.
    if check("the robot's gripper is to the side of the handle and the robot's gripper is not around handle"):
        robot.grab("handle")
    # Once the gripper is around the handle, we can just pull the handle up.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")
```