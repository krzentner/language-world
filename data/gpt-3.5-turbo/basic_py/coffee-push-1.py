# move-gripper: move the robot's gripper to a specific position
def move_gripper(robot, position):
    if check(f"the robot's gripper is not at {position}"):
        robot.move(f"gripper to {position}")

# button_press_sidedown: push the button from the side
def button_press_sidedown(robot):
    if check("the robot's gripper is not horizontally aligned with button and the robot's gripper is not to the left of the button"):
        robot.move("gripper to left of button")
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("the button down")

# drawer_open_second: pull the drawer open from the side
def drawer_open_side(robot):
    if check("the robot's gripper is not horizontally aligned with drawer handle and the robot's gripper is not to the left of the drawer handle"):
        robot.move("gripper to left of drawer handle")
    if check("the robot's gripper is horizontally aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.move("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")

# door_close: push the door close
def door_close(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.push("door closed")

# window_close_second: slide the window closed to the left
def window_close_side(robot):
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")

# peg_insert_top: grab the peg and insert it into the hole from the top
def peg_insert_top(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not below the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with hole"):
        robot.align("peg to hole")
    if check("peg is vertically aligned with hole"):
        robot.insert("peg into