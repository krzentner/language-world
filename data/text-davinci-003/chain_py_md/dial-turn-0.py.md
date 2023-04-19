

Then add the steps code:

```
    # Steps:
    #  1. Put gripper above dial
    #  2. Grab dial with gripper
    #  3. Turn dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not above dial"):
        robot.put("gripper above dial")
    # If the dial isn't below the gripper, grab it by moving the gripper down
    # around it.
    if check("the robot's gripper is not around dial and the robot's gripper is open"):
        robot.drop("gripper around dial")
    # Once the gripper is around the dial, we can just start turning it.
    if check("the robot's gripper is around dial"):
        robot.turn("dial")
```