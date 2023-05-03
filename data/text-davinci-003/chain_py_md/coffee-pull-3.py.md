

Solution:

```
# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above handle of mug
    #  2. Drop gripper around handle of mug
    #  3. Close gripper around handle of mug
    #  4. Pull mug to goal
    # First, put the gripper roughly above handle of mug, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the handle of mug"):
        robot.place("gripper above handle of mug")
    # If the gripper isn't around the handle of mug, put it around the mug handle.
    if check("the robot's gripper is not around handle of mug and the robot's gripper is open"):
        robot.drop("gripper around handle of mug")
    # If the gripper is near the handle of mug and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near handle of mug and the robot's gripper is open"):
        robot.close("gripper around handle of mug")
    # We closed the gripper, and the mug handle is still near the gripper, so 
    # maybe we grabbed it.
    # Try to move the mug to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around handle of mug and the robot's gripper is closed"):
        robot.pull("mug to goal")
```