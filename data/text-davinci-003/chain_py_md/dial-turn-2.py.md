

Then write the appropriate body of the function:

```
# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper above dial
    #  2. Drop gripper around dial 
    #  3. Push down on the dial 
    #  4. Turn the dial
    # We should put the gripper above the dial before we try to grab it, so that
    # we don't bump it by mistake. 
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    # As long as the gripper is still around the dial, grab it.
    if check("the robot's gripper is not around the dial"):
        robot.drop("gripper around dial")
    # Now the robot's gripper should be close to the dial and closed.
    # Push down on the dial to start turning it.
    if check("the robot's gripper is around dial and the robot's gripper is closed"):
        robot.push("down on dial")
    # Continue turning the dial until it's at the desired angle.
    if check("the dial is not at the target angle"):
        robot.turn("dial clockwise/counterclockwise")
```