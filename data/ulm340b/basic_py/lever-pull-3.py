
    if check("the robot's gripper is not above lever"):
        robot.move("gripper to above lever")
    if check("the robot's gripper is above lever"):
        robot.grasp("lever")
    if check("the robot's gripper is forward aligned with lever"):
        robot.turn("lever up")

# lever-push: rotate the lever down
def lever_push(robot):
    if check("the robot's gripper is not above lever"):
        robot.move("gripper to above lever")
    if check("the robot's gripper is above lever"):
        robot.grasp("lever")
    if check("the robot's gripper is forward aligned with lever"):
        robot.turn("lever down")

# peg-unstack-side: pull the peg out of the hole from the side
def peg_unstack_side(robot):
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move("gripper above peg")
    if check("peg is vertically aligned with the robot's gripper"):
        robot.grasp("peg")
    if check("the robot's gripper is forward aligned with peg"):
        robot.pull("peg from hole")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around peg"):
        robot.grasp("peg")
    if check("peg is vertically aligned with hole and peg is not forward aligned with the robot's gripper"):
        robot.align("peg to hole")
    if check("peg is vertically aligned with the robot's gripper and peg is forward aligned with hole"):
        robot.insert("peg into hole")

# button-press-side: push the button from the side
def button_press_side(robot):
    if check("the robot's gripper is not right of button"):
        robot.grab("the button")
    if check("the robot's gripper is forward aligned with button"):
        robot.push("down on the button")

# peg-unstack