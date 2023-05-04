
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.grab("box lid")
    if check("the robot's gripper is above the box and the robot's gripper is closed"):
        robot.place("box lid on box")

# box-open: pick up the box lid and place it behind the box
def box_open(robot):
    if check("the robot's gripper is not above box lid"):
        robot.move("gripper above box lid")
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.pick("up box lid")
    if check("the robot's gripper is above the box and the robot's gripper is closed"):
        robot.place("box lid behind box")

# stack: pick up the blue puck and put it on the red puck
def stack(robot):
    if check("the robot's gripper is not above the blue puck"):
        robot.place("gripper above blue puck")
    if check("the robot's gripper is not around the blue puck and the robot's gripper is open"):
        robot.grab("blue puck")
    if check("the robot's gripper is above the red puck and the robot's gripper is closed"):
        robot.place("blue puck on red puck")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is not left of the peg and the robot's gripper is not forward aligned with the peg"):
        robot.pick("up peg")
    if check("peg is forward aligned with the robot's gripper and peg is not horizontally aligned with hole"):
        robot.align("peg with hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not left of door handle"):
        robot.