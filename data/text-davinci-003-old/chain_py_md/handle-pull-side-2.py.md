

The program should look like this:

```
# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper on the side of the handle
    #  2. Pull up the handle
    # First, put the gripper to the side of the handle.
    if check("the robot's gripper is not right of the handle"):
        robot.put("gripper right of handle")
    # Now we can try to pull the handle up with the gripper.
    if check("the robot's gripper is right of the handle"):
        robot.pull("the handle up")
```