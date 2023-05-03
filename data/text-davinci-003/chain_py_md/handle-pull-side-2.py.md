

The steps for this task are as follows:

1. Put gripper above the handle
2. Grab the handle with the gripper 
3. Pull the handle up from the side 

Solution:
```
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper 
    #  3. Pull the handle up from the side 
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # If the handle becomes left of the gripper, go back to putting the gripper
    # above the handle. 
    # Because the handle is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    # As long the gripper is still mostly around the handle, pull the handle
    # up from the side.
    if check("the robot's gripper is around the handle"):
        robot.pull("handle up from the side")
```