
    if check("the robot's gripper is above the window handle"):
        robot.place("gripper right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with the door handle and the robot's gripper is below the door handle"):
        robot.move("gripper to right of door handle")
    if check("the robot's gripper is near the door handle"):
        robot.slide("door right")
    if check("the robot's gripper is in front of the door handle"):
        robot.push("door right harder")


# button-press-side: push the button from the side
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.place("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button sideways")

# peg-unplug-side: grab the peg and remove it from the hole from the side
def peg_unplug_side(robot):
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is vertically aligned with peg"):
        robot.push("peg rightwards")

# pick-place-side: grab the puck and place it to the side
def pick_place_side(robot):
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is not around puck"):
        robot.grab("puck")
    if check("the robot's gripper is around puck"):
        robot.put("puck at goal")


# peg-insert-side-v2: grab the peg and insert it into the hole from the side, v2
def peg_insert_side_v2(robot):
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.move("gripper above peg")
    if check