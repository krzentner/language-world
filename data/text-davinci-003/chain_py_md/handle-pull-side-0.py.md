

Solution:

```
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper beside handle
    #  2. Line up gripper with handle
    #  3. Grab handle
    #  4. Pull handle up
    # Put the gripper to the side of the handle.
    if check("the robot's gripper is not beside handle"):
        robot.put("gripper beside handle")
    # Once the gripper is beside the handle, we can line up the gripper with the
    # handle.
    if check("the robot's gripper is beside handle and the robot's gripper is not aligned with handle"):
        robot.align("gripper to handle")
    # If the gripper is lined up with the handle, grab it.
    if check("the robot's gripper is aligned with handle and the robot's gripper is open"):
        robot.grab("handle")
    # Once the handle is grabbed, pull up the handle.
    if check("the robot's gripper is aligned with handle and the robot's gripper is closed"):
        robot.pull("up handle")
 ```