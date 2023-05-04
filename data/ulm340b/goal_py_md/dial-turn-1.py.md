

Once you've written a program for `dial-turn`, you can start the robot running:

```
def dial_turn(robot):
    # Steps:
    #  1. Put gripper vertically above dial
    #  2. Lower gripper around the dial
    #  3. Close gripper around dial
    #  4. Turn the dial
    # Move the gripper over the dial.
    if check("the robot's gripper is not almost vertically aligned with the dial"):
        robot.move_gripper("almost vertically aligned with the dial")
    # Lower the gripper around the dial.
    # We can't lower the gripper below the dial because the robot's base is in
    # the way, so make sure we're around the dial before we close the gripper.
    if check("the robot's gripper is not almost around the dial"):
        robot.move_gripper("almost around the dial")
    # Close the gripper around the dial.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Now that the gripper is closed around the dial, we can rotate it.
    if check("the robot's gripper is closed around the dial"):
        robot.move_gripper("on the other side of the dial")

robot = Robot()

while True:
    dial_turn(robot)
    robot.draw_state()
```
'''

# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper vertically above dial
    #  2. Lower gripper around the dial
    #  3. Close gripper around dial
    #  4. Turn the dial
    # Move the gripper over the dial.
    if check("the robot's gripper is not almost vertically aligned with the dial"):
        robot.move_gripper("almost vertically aligned with the dial")
    # Lower the gripper around the dial.
    # We can't lower the gripper below the dial because the robot's base is in
    # the way, so make sure we're around the dial before we close the gripper.
    if check("the robot's gripper is not almost around the dial