

and add lines after that to complete the function.

If you get stuck, you can type `help` to see this message again,
`examples` to see other examples, `hint` to get a hint,
or `solution` to see a solution.
''',
'''
# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")
''',
'''
# disassemble: pull the wrench off the peg
def disassemble(robot):
    if check("the robot's gripper is not vertically aligned with wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is vertically aligned with wrench and the wrench is not horizontally aligned with wrench"):
        robot.align("wrench to wrench")
    if check("the wrench is horizontally aligned with wrench"):
        robot.push("wrench down")
''',
'''
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
''',
'''
# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if