

The function should move the robot's gripper to succeed at the task: pull up the handle.

```
# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up the handle
    # First, put the gripper roughly above handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.move_gripper("near the handle", close_gripper=True)
    # If the gripper is near the handle and closed, pull up on the handle.
    if check("the robot's gripper is around handle and the robot's gripper is closed"):
        robot.move_gripper("above the handle")
```