

The goal is to rotate the lever up, so the code that follows should have the robot take the steps needed to accomplish this.

```
# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put gripper above the lever
    #  2. Drop gripper around the lever
    #  3. Rotate the lever up
    # First, put the gripper where it can reach the lever.
    if check("the robot's gripper is not near the lever"):
        robot.move_gripper("near the lever")
    # Once the gripper is near the lever, we should be able to grab it and rotate
    # it.
    if check("the robot's gripper is close to the lever and the robot's gripper is not around lever"):
        robot.move_gripper("around the lever")
    # Once the gripper is around the lever, we should be able to rotate it.
    if check("the robot's gripper is around lever"):
        robot.move_gripper("vertically aligned with the lever")
```