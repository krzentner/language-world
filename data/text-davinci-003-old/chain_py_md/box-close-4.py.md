

Steps:
1. Put the gripper above the lid
2. Grab the lid with the gripper
3. Place the lid on the box

```
# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Put the gripper above the lid
    if check("the robot's gripper is not above the lid"):
        robot.put("gripper above lid")
    #  2. Grab the lid with the gripper
    if check("the robot's gripper is above the lid and the robot's gripper is not around the lid"):
        robot.grab("lid")
    #  3. Place the lid on the box
    if check("the robot's gripper is around the lid"):
        robot.place("lid onto box")
```