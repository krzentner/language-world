
    if check("the robot's gripper is not near faucet handle"):
        robot.grab("faucet handle")
    if check("the robot's gripper is near faucet handle"):
        robot.turn("faucet left")

# faucet-close: turn the faucet right
def faucet_close(robot):
    if check("the robot's gripper is not near faucet handle"):
        robot.grab("faucet handle")
    if check("the robot's gripper is near faucet handle"):
        robot.turn("faucet right")

# button-press-side: press the button from the side
def button_press_side(robot):
    if check("the robot's gripper is not right of button and the robot's gripper is not near button"):
        robot.put("gripper to right of button")
    if check("the robot's gripper is right of button and the robot's gripper is not near button"):
        robot.push("gripper into button")
    if check("the robot's gripper is not forward aligned with button and the robot's gripper is not near button"):
        robot.put("gripper near button")
    if check("the robot's gripper is forward aligned with button and the robot's gripper is near button"):
        robot.push("down on button")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is near the door handle"):
        robot.push("door closed")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# ================================
# TASK
# ================================

# Define the task