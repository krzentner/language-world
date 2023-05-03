

Steps:
1. Put gripper above handle
2. Drop gripper around handle
3. Pull up on handle

```
# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up on handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is around the handle, pull up on the handle.
    if check("the robot's gripper is around handle"): 
        robot.pull("up on handle")
```