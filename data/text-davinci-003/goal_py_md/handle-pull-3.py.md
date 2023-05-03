

Answer:

```
# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper below handle
    #  2. Push the gripper up to grab the handle
    #  3. Pull the handle up
    # First, we need to put the gripper below the handle.
    if check("the robot's gripper is not below the handle"): 
        robot.move_gripper("below the handle", close_gripper=True)
    # Once the gripper is below the handle, we need to move the gripper up to 
    # grab the handle.
    if check("the robot's gripper is below the handle and the robot's gripper is open"):
        robot.move_gripper("near the handle")
    # If the gripper is near the handle, close the gripper around the handle.
    if check("the robot's gripper is near the handle and the robot's gripper is closed"):
        robot.move_gripper("above the handle")
    # Once the handle is grabbed, move the handle up.
    if check("the robot's gripper is above the handle"):
        robot.move_gripper("above the target location")
```
