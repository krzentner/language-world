

Then complete the task:

```
# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Step:
    #  1. Put gripper below handle
    #  2. Grab handle with gripper
    #  3. Pull up handle
    # Put the gripper below the handle so that we don't have to line up the gripper precisely.
    if check("the robot's gripper is not below the handle"):
        robot.move_gripper("below the handle", close_gripper=True)
    # If the gripper is below the handle and the gripper is open,
    # we can grab the handle by closing the gripper.
    if check("the robot's gripper is below the handle and the robot's gripper is not closed"):
        robot.move_gripper("near the handle")
    # If the handle is trapped, we can pull it up.
    if check("the robot's gripper is near the handle and the robot's gripper is closed"):
        robot.move_gripper("above the handle")
```