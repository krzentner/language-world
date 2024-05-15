

The steps of the task are:
1. Put gripper above handle
2. Drop gripper around handle
3. Pull up the handle

```
# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up the handle
    # Put the gripper roughly above handle so that it doesn't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the handle"):
        robot.place("gripper above handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is near the handle and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    # We closed the gripper, and the handle is still near the gripper, so maybe
    # we grabbed it.
    # If we grabbed it, try to pull the handle up.
    if check("the robot's gripper is above handle and the robot's gripper is closed"):
        robot.pull("handle up")
```