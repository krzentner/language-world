

The dial-turn program is used to turn a dial by a specified amount.

Steps:
 1. Put gripper above dial
 2. Grab the dial with the gripper
 3. Turn dial

First, the robot should put its gripper above the dial. We can do this using a `put` command.

```
# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper above dial
    #  2. Grab the dial with the gripper
    #  3. Turn dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
```

Next, the robot can grab the dial with the gripper. We can do this using a `grab` command.

```
# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper above dial
    #  2. Grab the dial with the gripper
    #  3. Turn dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")

    # If the dial is left of the gripper, grab the dial with the gripper.
    if check("dial is not left of the robot's gripper and dial is not forward aligned with the robot's gripper"):
        robot.grab("dial")
```

Finally, the robot can turn the dial. We can do this using a `turn` command.

```
# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper above dial
    #  2. Grab the dial with the gripper
    #  3. Turn dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")

    # If the dial is left of the gripper, grab the dial with the gripper.
    if check("dial is not left of the robot's gripper and dial is not forward aligned with the robot's gripper"):
        robot.grab("dial")

    # If the gripper is forward aligned with the dial, turn the dial.
    if check("the robot's gripper is forward aligned with the dial"):
        robot.turn("dial")
```