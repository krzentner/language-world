

The steps required to pull the handle from the side are:
1. Put gripper above the handle
2. Drop gripper around handle
3. Pull up the handle

```
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop gripper around handle
    #  3. Pull up the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the handle and the robot's gripper is open"):
        robot.put("gripper around handle")
    # As long as the gripper is still lined up with the handle, it's being pulled,
    # so keep pulling.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.pull("handle up")
``