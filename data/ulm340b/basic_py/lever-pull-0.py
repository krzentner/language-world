
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is vertically aligned with lever and lever is not right of the robot's gripper"):
        robot.close("gripper around lever")
    if check("the robot's gripper is right of lever"):
        robot.pull("down and rotate lever up")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# button-press-side: push the button down from the side
def button_press_side(robot):
    if check("button is not left of the robot's gripper and the robot's gripper is open"):
        robot.close("gripper around button")
    if check("the robot's gripper is forward aligned with button and button is not left of the robot's gripper"):
        robot.push("down on button")

# peg-unstack-side: unstack the pegs from the side
def peg_unstack_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg"):
        robot.lift("peg up")
    if check("peg is not in a stack"):
        robot.drop("peg on goal")

# peg-unstack-topdown: unstack the peg from above
def peg_unstack_topdown(robot):
    if check("peg is not below the robot's gripper"):
        robot.put("gripper above peg")
    if check("peg is below the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with peg"):
        robot.lift("peg up")
    if check("peg is not in a stack"):
        robot.drop("peg on