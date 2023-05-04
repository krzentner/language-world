
    if check("the robot's gripper is not near faucet and the robot's gripper is open"):
        robot.grab("faucet")
    if check("the robot's gripper is near faucet"):
        robot.turn("faucet left")

# drawer-close-side: push the drawer closed from the side
def drawer_close_side(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# knob-turn-cw: turn the knob clockwise
def knob_turn_cw(robot):
    if check("the robot's gripper is not around knob"):
        robot.grab("knob")
    if check("the robot's gripper is around knob"):
        robot.turn("knob clockwise")

# hook-pull: grab the hook and pull it upwards
def hook_pull(robot):
    if check("the robot's gripper is not forward aligned with hook and the robot's gripper is not around hook"):
        robot.grab("hook")
    if check("the robot's gripper is around hook"):
        robot.lift("hook up")

# window-open-side: push the window open to the left from the side
def window_open_side(robot):
    if check("the robot's gripper is not near the window handle"):
        robot.grab("window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")

# peg-insert-sideway: grab the peg and insert it into the hole from the side
def peg_insert_sideway(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
