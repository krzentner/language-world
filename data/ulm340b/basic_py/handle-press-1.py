
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("handle down")

# door-unlock: push the door unlock button to the left
def door_unlock(robot):
    if check("the robot's gripper is right of the door unlock button and the robot's gripper is not near the door unlock button"):
        robot.move("gripper left")
    if check("the robot's gripper is near the door unlock button"):
        robot.push("unlock to the left")
    if check("the robot's gripper is in front of the door unlock button"):
        robot.push("unlock harder")

# light-switch-on: flip the light switch up to turn on the light
def light_switch_on(robot):
    if check("the robot's gripper is below the light switch and the robot's gripper is not near the light switch"):
        robot.grab("light switch")
    if check("the robot's gripper is near the light switch"):
        robot.flip("switch up")
    if check("the robot's gripper is in front of the light switch"):
        robot.flip("switch up hard")

# peg-unstack: remove the top peg from the stack
def peg_unstack(robot):
    if check("the robot's gripper is not vertically aligned with the top peg"):
        robot.put("gripper above top peg")
    if check("the robot's gripper is vertically aligned with the top peg"):
        robot.lift("peg up")

# peg-insert-sideway: grab the peg and insert it into the hole from the side
def peg_insert_sideway(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# lever-pull: pull the lever down
