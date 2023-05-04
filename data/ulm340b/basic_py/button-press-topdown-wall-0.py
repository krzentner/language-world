
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is not left of button"):
        robot.put("gripper left of button")
    if check("the robot's gripper is left of button and the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# button-press-side: push the button from the left
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper left of button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not forward aligned with the button"):
        robot.place("gripper forward of button")
    if check("the robot's gripper is forward aligned with the button"):
        robot.push("button left")

# peg-insert-side-wall: grab the peg and insert it into the hole from the side, with a wall in the way
def peg_insert_side_wall(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the peg is not left of the robot's gripper and the peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("the peg is horizontally aligned with hole"):
        robot.insert("peg into hole")


# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with the door handle"):
        robot.push("door closed")

# pick-place-wall: pick up the puck and hold it at the target location, with a short wall in the way
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's grip