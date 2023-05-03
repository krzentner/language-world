

We want the robot to perform the task of turning a dial. To do this, the following steps need to be taken:

1. Put gripper above dial handle
2. Drop gripper around dial handle
3. Turn the dial clockwise or counterclockwise

```
# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper above dial handle
    #  2. Drop gripper around dial handle
    #  3. Turn the dial clockwise or counterclockwise
    # Let's first put the gripper above the dial handle.
    if check("the robot's gripper is not vertically aligned with the dial handle"):
        robot.move_gripper("vertically aligned with the dial handle")
    # Then, line up the gripper with the handle so that it can grab it.
    if check("the robot's gripper is not around the dial handle"):
        robot.move_gripper("around the dial handle", close_gripper=True)
    # Finally, turn the dial in the desired direction.
    if check("the robot's gripper is around the dial handle"):
        robot.move_gripper("clockwise around the dial handle")
        # or
        robot.move_gripper("counterclockwise around the dial handle")
```