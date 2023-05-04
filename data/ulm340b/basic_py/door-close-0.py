
    if check("the robot's gripper is not above the door handle and the robot's gripper is not vertically aligned with the door handle"):
        robot.put("the gripper above the door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not near the door handle"):
        robot.push("the gripper into the door handle")
    if check("the robot's gripper is near the door handle and the door handle is below the robot's gripper"):
        robot.slide("the door handle to the goal")

# knob-turn-left: grab the doorknob and rotate it left
def knob_turn_left(robot):
    if check("the robot's gripper is not around the doorknob"):
        robot.put("gripper around doorknob")
    if check("the robot's gripper is around the doorknob"):
        robot.turn("knob left")

# knob-turn-right: grab the doorknob and rotate it right
def knob_turn_right(robot):
    if check("the robot's gripper is not around the doorknob"):
        robot.put("gripper around doorknob")
    if check("the robot's gripper is around the doorknob"):
        robot.turn("knob right")

# button-press-side: press down on the button from the left
def button_press_side(robot):
    if check("the robot's gripper is not left of button and the robot's gripper is not forward aligned with button"):
        robot.push("gripper left of button")
    if check("the robot's gripper is forward aligned with button"):
        robot.push("down on button")

# button-press-forward: push the button down from in front of it
def button_press_forward(robot):
    if check("the robot's gripper is not forward aligned with button"):
        robot.move("gripper infront of button")
    if check("the robot's gripper is forward aligned with button"):
        robot.push("down on button")

# peg-unstack-side: remove the top peg from the bottom peg
def peg_unstack_side(robot):
    if check("the robot's gripper is not above the top peg"):
        robot.move("gripper above top peg")
    if check("the robot's gripper is above the top peg and the robot's