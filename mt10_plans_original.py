# reach: reach to the target location
def reach(robot):
    if check("reach target is mostly below the robot's gripper"):
        robot.reach("to goal")
    if check("reach target is not right of the robot's gripper"):
        robot.reach("to goal")


# push: grab the puck and move it to the target location
def push(robot):
    if check("puck is not below the robot's gripper"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is not above puck"):
        robot.put("the gripper above the puck")
    if check("puck is below the robot's gripper and puck is not near the robot's gripper"):
        robot.push("the gripper into the puck")
    if check("puck is below the robot's gripper and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("puck is near the robot's gripper and puck is below the robot's gripper"):
        robot.slide("the puck to the goal")
    if check("puck is near the robot's gripper and the robot's gripper is above puck"):
        robot.slide("the puck to the goal")


# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    if check("puck is not below the robot's gripper"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("puck is below the robot's gripper and gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is above puck and gripper is open"):
        robot.drop("gripper around puck")
    if check("puck is near the robot's gripper and gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is near puck and gripper is open"):
        robot.close("gripper around puck")
    if check("puck is below the robot's gripper and gripper is closed"):
        robot.place("puck at goal")
    if check("the robot's gripper is above puck and gripper is closed"):
        robot.place("puck at goal")


# door-open: pull the door open
def door_open(robot):
    if check("door handle is not almost vertically aligned with the robot's gripper"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("door handle is left of the robot's gripper and gripper is closed"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is right of door handle and gripper is closed"):
        robot.put("gripper around door handle")
    if check("door handle is vertically aligned with the robot's gripper and door handle is not left of the robot's gripper"):
        robot.push("door closed")
    if check("door handle is vertically aligned with the robot's gripper and the robot's gripper is not right of door handle"):
        robot.push("door closed")


# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("drawer handle is not vertically aligned with the robot's gripper"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("drawer handle is vertically aligned with the robot's gripper and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")
    if check("drawer handle is vertically aligned with the robot's gripper and the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")


# drawer-close: push the drawer close
def drawer_close(robot):
    if check("gripper is open"):
        robot.put("the gripper in front of the drawer")
    if check("drawer handle is vertically aligned with the robot's gripper and gripper is open"):
        robot.put("the gripper in front of the drawer")
    if check("drawer handle is below the robot's gripper"):
        robot.put("the gripper above the drawer handle")
    if check("the robot's gripper is above drawer handle"):
        robot.put("the gripper above the drawer handle")
    if check("drawer handle is not vertically aligned with the robot's gripper and drawer handle is not forward aligned with the robot's gripper"):
        robot.grab("drawer handle")
    if check("drawer handle is not vertically aligned with the robot's gripper and the robot's gripper is not forward aligned with drawer handle"):
        robot.grab("drawer handle")
    if check("drawer handle is forward aligned with the robot's gripper"):
        robot.push("drawer closed")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")


# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("button is not vertically aligned with the robot's gripper"):
        robot.put("gripper above button")
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("button is vertically aligned with the robot's gripper"):
        robot.push("down on button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")


# peg-insert-side: insert the peg into the hole from the side
def peg_insert_side(robot):
    if check("peg is left of the robot's gripper"):
        robot.put("gripper above peg")
    if check("the robot's gripper is right of peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("peg is not left of the robot's gripper and the robot's gripper is not forward aligned with peg"):
        robot.grab("peg")
    if check("peg is forward aligned with the robot's gripper and peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is forward aligned with the robot's gripper and hole is not horizontally aligned with peg"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")
    if check("hole is horizontally aligned with peg"):
        robot.insert("peg into hole")


# window-open: slide the window open
def window_open(robot):
    if check("window handle is not vertically aligned with the robot's gripper and the robot's gripper is mostly below window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is mostly below window handle and window handle is not vertically aligned with the robot's gripper"):
        robot.move("gripper to right of window handle")
    if check("window handle is left of the robot's gripper and window handle is vertically aligned with the robot's gripper"):
        robot.slide("window left")
    if check("window handle is left of the robot's gripper and window handle is almost vertically aligned with the robot's gripper"):
        robot.slide("window left")
    if check("window handle is near the robot's gripper"):
        robot.push("window left harder")
    if check("window handle is behind the robot's gripper"):
        robot.push("window left harder")


# window-close: slide the window closed
def window_close(robot):
    if check("window handle is not vertically aligned with the robot's gripper"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is not vertically aligned with window handle"):
        robot.move("gripper to left of window handle")
    if check("window handle is right of the robot's gripper"):
        robot.slide("window right")
    if check("the robot's gripper is left of window handle"):
        robot.slide("window right")
    if check("window handle is vertically aligned with the robot's gripper and window handle is not right of the robot's gripper"):
        robot.push("window right harder")
    if check("window handle is vertically aligned with the robot's gripper and the robot's gripper is not left of window handle"):
        robot.push("window right harder")


