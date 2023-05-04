
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with peg"):
        robot.pull("peg out")

# peg-unplug-topdown: grab the peg and pull the it out from above
def peg_unplug_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is not around peg"):
        robot.put("gripper around peg")
    if check("the robot's gripper is vertically aligned with peg"):
        robot.pull("peg out")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is not around peg"):
        robot.put("gripper around peg")
    if check("the robot's gripper is around peg"):
        robot.insert("peg into hole")

# turn-switch-on: rotate the knob so that it is horizontal
def turn_switch_on(robot):
    if check("the robot's gripper is not vertically aligned with the switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is vertically aligned with switch and the robot's gripper is not around switch"):
        robot.put("gripper around switch")
    if check("the robot's gripper is around switch"):
        robot.turn("switch to on position")

# turn-switch-off: rotate the knob so that it is vertical
def turn_switch_off(robot):
    if check("the robot's gripper is not vertically aligned with the switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is vertically aligned with switch and the robot's gripper is not around switch"):
        robot