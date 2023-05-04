

```
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

Here's some code that demonstrates how the robot can do a variety of tasks:

```
# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper above the knob
    #  2. Grab the knob
    #  3. Turn the knob counter-clockwise
    # If the knob is not below the robot's gripper as seen from above, move the
    # gripper above the knob.
    if check("the robot's gripper is not above knob and the robot's gripper is not vertically aligned with knob"):
        robot.put("gripper above knob")
    # If the knob is above the gripper as seen from above, put the gripper
    # around the knob to grab it.
    if check("the robot's gripper is vertically aligned with knob and the robot's gripper is not around knob"):
        robot.grab("knob")
    # If the gripper is lined up with the knob as seen from the left and the
    # gripper is not open, turn the faucet left.
    if check("the robot's gripper is not horizontally aligned with knob and the robot's gripper is not open"):
        robot.turn("faucet left")

# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper above the knob
    #  2. Grab the knob
    #  3. Turn the knob clockwise
    # If the knob is not below the robot's gripper as seen from above, move the
    # gripper above the knob.
    if check("the robot's gripper is not above knob and the robot's gripper is not vertically aligned with knob"):
        robot.put("gripper above knob")
    # If the knob is above the gripper as seen from above, put the gripper
    # around the knob to grab it.
    if check("the robot's gripper is vertically aligned with knob and the robot's gripper is not around knob"):
        robot.grab("knob")
    # If the gripper is lined up with the knob as seen from the left and the
    # gripper is