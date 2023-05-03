

```
# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    #  1. Put the gripper above the dial
    #  2. Align the robot's gripper with the dial
    #  3. Turn the dial with the robot's gripper
    # Put the gripper above the dial.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial")
    # Align the robot's gripper with the dial.
    if check("the robot's gripper is not horizontally aligned with the dial"):
        robot.move_gripper("horizontally aligned with the dial")
    # Once the gripper is aligned with the dial, close the gripper while gently
    # applying pressure to begin turning the dial.
    if check("the robot's gripper is horizontally aligned with the dial and the robot's gripper is not closed"):
        robot.move_gripper("near the dial", close_gripper=True)
    # Once the gripper is closed, move the gripper left or right in a gentle
    # motion to turn the dial depending on the desired direction.
    if check("the robot's gripper is closed"):
        robot.move_gripper("left/right of the dial")
```