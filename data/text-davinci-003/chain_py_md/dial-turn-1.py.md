

Then add the following code to your program:

```
    # Steps:
    #  1. Put gripper above the dial
    #  2. Drop gripper around dial
    #  3. Turn the dial
   
    # First, put the gripper roughly above the dial, then line it up.
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.put("gripper above dial")
    # If the gripper is not entirely around the dial, and open, put the gripper
    # around the dial.
    if check("the robot's gripper is not around dial and the robot's gripper is open"):
        robot.drop("gripper around dial")
    # If the gripper is around the dial and closed, rotate the dial.
    if check("the robot's gripper is around dial and the robot's gripper is closed"):
        robot.rotate("dial")
```