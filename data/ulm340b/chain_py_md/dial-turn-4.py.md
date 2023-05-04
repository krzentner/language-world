

This task can be accomplished using the following code:

```
# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Grab the dial and turn it
    # Because this is a dial, we can align it from the front.
    if check("the robot's gripper is not forward aligned with dial"):
        robot.put("gripper in front of dial")
    # Grab the dial and turn it left.
    if check("the robot's gripper is forward aligned with dial and the robot's gripper is open"):
        robot.close("gripper around dial")
    if check("the robot's gripper is around dial"):
        robot.twist("dial left")
```

"""

# Task: dial-turn
def dial_turn(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Grab the dial and turn it
    # Because this is a dial, we can align it from the front.
    if check("the robot's gripper is not forward aligned with dial"):
        robot.put("gripper in front of dial")
    # Grab the dial and turn it left.
    if check("the robot's gripper is forward aligned with dial and the robot's gripper is open"):
        robot.close("gripper around dial")
    if check("the robot's gripper is around dial"):
        robot.twist("dial left")


# Task: door-open
def door_open(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    #