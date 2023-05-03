```
# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put gripper roughly around lever handle
    #  2. Pull the lever up
    # First, put the gripper roughly around the lever handle.
    if check("the robot's gripper is not near the lever handle"):
        robot.grab("lever handle")
    # Once the gripper is around the lever handle, we can pull the lever up.
    # We don't need to be careful about the direction, since the lever can rotate
    # freely in either direction.
    if check("the robot's gripper is around lever handle"):
        robot.pull("lever up")
```