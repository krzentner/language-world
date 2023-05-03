

The code for the handle-pull-side task is:

```
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Line the handle up with the grip
    #  4. Pull the handle sideways 
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # Then, grab the handle with the gripper.
    if check("the robot's gripper is not around the handle"):
        robot.move_gripper("near the handle", close_gripper=True)
    # Once the handle is attached to the gripper, make sure it is lined up with
    # the grip.
    if check("the robot's gripper is not forward aligned with handle"):
        robot.move_gripper("forward aligned with the handle")
    # After the handle is aligned, pull the handle.
    if check("the robot's gripper is forward aligned with the handle"):
        robot.move_gripper("left of the handle")
```