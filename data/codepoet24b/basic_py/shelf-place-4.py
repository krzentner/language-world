# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open")

# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# window-close: slide the window closed to the right
def window_close(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

# window-open: slide the window open to the left
def window_open(robot):
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")

# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")

# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

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

# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    if check("the robot's gripper is empty and the robot's gripper is not above the block"):
        robot.place("gripper below block")
    if check("the robot's gripper is above the block"):
        robot.pick("up block")
    if check("the robot's gripper is below the block and the robot's gripper is not closed"):
        robot.close("gripper around block")
    if check("robot's gripper is closed and the robot's gripper is above the shelf"):
        robot.place("block on shelf")

# shelf-align: align the robot's gripper position with the target location on the shelf
def shelf_align(robot):
    if check("the robot's gripper is not vertically aligned with the shelf"):
        robot.put("gripper above shelf")
    if check("the robot's gripper is vertically aligned with the shelf"):
        robot.align("gripper to target location")

# align-cube: align the robot's gripper position with the target location on the cube
def align_cube(robot):
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube"):
        robot.align("gripper to target location")

# align-block: align the robot's gripper position with the target location on the block
def align_block(robot):
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.put("gripper above block")
    if check("the robot's gripper is vertically aligned with the block"):
        robot.align("gripper to target location")

# put-cube-on-block: place the robot's gripper on top of the block and close it
def put_cube_on_block(robot):
    if check("the robot's gripper is not above the block and the robot's gripper is not vertically aligned with the block"):
        robot.place("gripper above block")
    if check("the robot's gripper is above the block and the robot's gripper is not vertically aligned with the block"):
        robot.align("gripper to block")
    if check("the robot's gripper is vertically aligned with the block"):
        robot.close("gripper on block")

# put-block-on