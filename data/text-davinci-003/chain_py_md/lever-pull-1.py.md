

After that, the program should be:
```
# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put gripper above the lever
    #  2. Trap the lever with the gripper
    #  3. Rotate the lever up
    # First, put the gripper above the lever.
    if check("the robot's gripper is not above the lever"):
        robot.put("gripper above lever")
    # If the gripper isn't around the lever, put it around the lever.
    if check("the robot's gripper is not around lever"):
        robot.grab("lever")
    # If the gripper is around the lever, we can try to rotate it up.
    if check("the robot's gripper is around the lever"):
        robot.rotate("lever up")
```