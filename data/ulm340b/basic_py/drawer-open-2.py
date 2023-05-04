
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.pull("drawer open")

# peg-remove-side: grab the peg and remove it from the hole from the side
def peg_remove_side(robot):
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is above the peg"):
        robot.remove("peg from hole")

# light-switch-on: push the light switch up
def light_switch_on(robot):
    if check("the robot's gripper is not vertically aligned with the light switch"):
        robot.put("gripper above light switch")
    if check("the robot's gripper is vertically aligned with the light switch"):
        robot.push("up on light switch")

# handle-pull: pull the handle towards you
def handle_pull(robot):
    if check("the robot's gripper is not forward aligned with the handle"):
        robot.grab("the handle")
    if check("the robot's gripper is forward aligned with the handle"):
        robot.pull("the handle towards you")

# light-switch-off: push the light switch down
def light_switch_off(robot):
    if check("the robot's gripper is not vertically aligned with the light switch"):
        robot.put("gripper above light switch")
    if check("the robot's gripper is vertically aligned with the light switch"):
        robot.push("down on light switch")

# lever-pull: pull the lever down
def lever_pull(robot):
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is vertically aligned with lever"):
        robot.push("down on lever")

# lever-push: push the lever up
def lever_push(robot):
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is vertically aligned with lever"):
        robot.pull("up on lever")

# faucet-pull: pull the faucet towards you
def faucet_pull(robot):