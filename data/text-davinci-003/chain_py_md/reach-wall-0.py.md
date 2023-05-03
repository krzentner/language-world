

Then it can be continued with:

```
    # Steps:
    #  1. Put gripper above wall
    #  2. Push gripper into wall
    #  3. Reach towards the target
    # Put the gripper above the wall, so we don't bump into it while trying to
    # move around it.
    if check("the robot's gripper is not above the wall"):
        robot.put("gripper above wall")
    # If the gripper isn't near the wall, put it near the wall.
    if check("the robot's gripper is not near wall"):
        robot.push("gripper into wall")
    # If the gripper is near the wall, maybe we've been able to move around it
    # and towards the target. 
    if check("the robot's gripper is near the wall"):
        robot.reach("to goal")
```