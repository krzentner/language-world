

Then fill in the code below:

```
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull up the handle from the side
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the handle is left of the gripper, go back to putting the gripper
    # above the handle.
    # Because the handle is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("the handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the handle", close_gripper=True)
    # As long the gripper is still mostly around the handle, pull it up.
    if check("the handle is horizontally aligned with the robot's gripper"):
        robot.move_gripper("above the handle")
```