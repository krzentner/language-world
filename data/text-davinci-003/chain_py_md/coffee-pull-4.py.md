

Then add your code for this task below:

```
# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Place the gripper near the mug handle
    #  2. Grab the mug handle with the gripper
    #  3. Pull the mug to the goal
    # If the the mug handle is not near the robot's gripper, move the gripper
    # near the mug handle.
    if check("the mug handle is not near the robot's gripper"):
        robot.move("gripper to near mug handle")
    # Once the gripper is near the mug handle, we should be able to
    # grab the mug handle by closing it around it.
    if check("the robot's gripper is near the mug handle and the robot's gripper is not closed"):
        robot.grab("mug handle")
    # Once the gripper is around the mug handle, we can just pull the mug to
    # the goal.
    if check("the robot's gripper is around the mug handle"):
        robot.pull("mug to goal")
```