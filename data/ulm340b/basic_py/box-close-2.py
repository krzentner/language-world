
    if check("the robot's gripper is not above lid"):
        robot.move("gripper above lid")
    if check("the robot's gripper is not around lid"):
        robot.put("gripper around lid")
    if check("the robot's gripper is around lid"):
        robot.lift("lid up")
    if check("the robot's gripper is not above box"):
        robot.put("lid above box")
    if check("the robot's gripper is around lid and the robot's gripper is above box"):
        robot.put("lid on box")

# lever-pull: pull the lever down
def lever_pull(robot):
    if check("the robot's gripper is not forward aligned with lever"):
        robot.put("gripper in front of lever")
    if check("the robot's gripper is forward aligned with lever"):
        robot.pull("lever down")

# button-press-side: push the button down from the side
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move("gripper over button")
    if check("the robot's gripper is not forward aligned with button and the robot's gripper is vertically aligned with button"):
        robot.put("gripper in front of button")
    if check("the robot's gripper is forward aligned with button"):
        robot.press("button down")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not below the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# box-open: pick up the box lid and place it off the box
def box_open(robot):
    if check("the robot's gripper is not vertically aligned with the box lid"):
        robot.put("gripper above lid")
