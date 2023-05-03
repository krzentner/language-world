

The code for this task is as follows:
```
# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put gripper roughly above lever handle
    #  2. Drop gripper around lever handle
    #  3. Rotate the lever upwards
    # We need to put the gripper roughly above the lever handle in order to line
    # it up correctly.
    if check("the robot's gripper is not almost vertically aligned with lever handle"):
        robot.move_gripper("almost vertically aligned with the lever handle")
    # Once the gripper is almost lined up, closing it should line it up all the
    # way correctly.
    if check("the robot's gripper is vertically aligned with the lever handle and the robot's gripper is not around lever handle"):
        robot.move_gripper("around the lever handle", close_gripper=True)
    # Once the gripper is around the lever handle, we can just rotate it upwards.
    if check("the robot's gripper is around lever handle"):
        robot.move_gripper("horizontally aligned with the lever handle")
```