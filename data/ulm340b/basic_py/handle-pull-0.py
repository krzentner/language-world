
    if check("the robot's gripper is not left of the handle and the robot's gripper is not near the handle"):
        robot.grab("the handle")
    if check("the robot's gripper is forward aligned with the handle"):
        robot.pull("the handle up")

# button-press: push the button
def button_press(robot):
    if check("the robot's gripper is not near the button"):
        robot.grab("the button")
    if check("the robot's gripper is near the button"):
        robot.push("the button down")

# toggle-switch: toggle the switch
def toggle_switch(robot):
    if check("the robot's gripper is not near the switch"):
        robot.grab("the switch")
    if check("the robot's gripper is near the switch"):
        robot.toggle("the switch up")

# latch-turn-left: turn the latch left
def latch_turn_left(robot):
    if check("the robot's gripper is not forward aligned with the latch"):
        robot.grab("latch handle")
    if check("the robot's gripper is near the latch"):
        robot.turn("latch handle left")

# latch-turn-right: turn the latch right
def latch_turn_right(robot):
    if check("the robot's gripper is not forward aligned with the latch"):
        robot.grab("latch handle")
    if check("the robot's gripper is near the latch"):
        robot.turn("latch handle right")

# peg-unstack: lift the peg up and place it down on the other side
def peg_unstack(robot):
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with the peg"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is around the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.lift("the peg up")
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.place("peg next to goal")

#