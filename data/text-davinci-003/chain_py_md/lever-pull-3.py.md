

Then add the following code:

```
    # Steps:
    #  1. Line up the gripper as viewed from the side
    #  2. Pull the lever up
    # To pull the lever up, we first need to line up the gripper from the side.
    if check("the robot's gripper is not horizontally aligned with lever"):
        robot.put("gripper left of lever")
    # Once the gripper is lined up, we can pull the lever up.
    if check("the robot's gripper is horizontally aligned with lever"):
        robot.pull("lever up")
```