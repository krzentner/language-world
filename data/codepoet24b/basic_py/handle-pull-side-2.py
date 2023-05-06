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

# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    if check("robot is not vertically aligned with handle and robot gripper is above handle"):
        robot.reach("to handle")
    if check("robot is vertically aligned with handle"):
        robot.rotate("sideways")
    if check("robot is facing the handle and robot gripper is horizontally aligned with handle"):
        robot.pull("handle up")

# ball-place-back: grab the ball and place it in the back corner of the table
def ball_place_back(robot):
    if check("the robot's gripper is not above the ball"):
        robot.reach("to ball")
    if check("the robot's gripper is above the ball and the ball is not under the robot's gripper"):
        robot.drop("ball")
    if check("the ball is under the robot's gripper"):
        robot.slide("ball to back")
    if check("the ball is in the back corner"):
        robot.place("ball in back corner")

# ball-place-side: grab the ball and place it in the side corner of the table
def ball_place_side(robot):
    if check("the robot's gripper is not above the ball"):
        robot.reach("to ball")
    if check("the robot's gripper is above the ball and the ball is not under the robot's gripper"):
        robot.drop("ball")
    if check("the ball is under the robot's gripper"):
        robot.slide("ball to side")
    if check("the ball is in the side corner"):
        robot.place("ball in side corner")

# ball-place-corner: grab the ball and place it in the corner of the table
def ball_place_corner(robot):
    if check("the robot's gripper is not above the ball"):
        robot.reach("to ball")
    if check("the robot's gripper is above the ball and the ball is not under the robot's gripper"):
        robot.drop("ball")
    if check("the ball is under the robot's gripper"):
        robot.slide("ball to corner")
    if check("the ball is in the corner"):
        robot.place("ball in corner")

# peg-insert-front: grab the peg and insert it into the hole from the front
def peg_insert_front(robot):
    if check("the robot's gripper is not vertically