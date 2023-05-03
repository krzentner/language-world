

The code should look like this:

```
# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Drop gripper around the mug
    #  3. Close the gripper around the mug
    #  4. Pull the mug towards the goal
    # First, put the gripper above the mug.
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above mug")
    # Then, drop the gripper around the mug.
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    # If the gripper is near the mug and open, close the gripper around it.
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    # Now that the mug is in the gripper, the robot can pull it towards the
    # goal.
    if check("the robot's gripper is around the mug and the robot's gripper is closed"):
        robot.pull("mug towards goal")
```