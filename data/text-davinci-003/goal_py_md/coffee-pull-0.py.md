

Here's the code for coffee-pull:

```
# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above coffee mug
    #  2. Put gripper around coffee mug
    #  3. Pull the mug towards the target location
    # First, we need to put the gripper above the coffee mug.
    if check("the robot's gripper is not roughly above the mug"):
        robot.move_gripper("above the mug")
    # Once the gripper is almost above the mug, we can put it around the mug.
    if check("the robot's gripper is not around the mug"):
        robot.move_gripper("near the mug", close_gripper=True)
    # Now that the gripper is around the mug, we can pull it towards the target 
    # location.
    if check("the robot's gripper is around mug"):
        robot.move_gripper("near the target location")
```