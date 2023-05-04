
    if check("the robot's gripper is not above coffee button"):
        robot.put("gripper above coffee button")
    if check("the robot's gripper is vertically aligned with coffee button"):
        robot.push("coffee button")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is near the door handle and the robot's gripper is open"):
        robot.close("gripper around door handle")
    if check("the robot's gripper is near the door handle and the robot's gripper is closed"):
        robot.push("door closed")

# peg-insert-front: grab the peg and insert it into the hole from the front
def peg_insert_front(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# valve-turn-right: turn the valve to the right
def valve_turn_right(robot):
    if check("the robot's gripper is not above valve handle"):
        robot.put("gripper above valve handle")
    if check("the robot's gripper is vertically aligned with the valve handle"):
        robot.grab("valve handle")
    if check("the robot's gripper is forward aligned with valve handle and valve is horizontal"):
        robot.turn("valve right")

# valve-turn-left: turn the valve to the left
def valve_turn_left(robot):
    if check("the robot's gripper is not above valve handle"):
        robot.put("gripper above valve handle")
    if check("the robot's gripper is vertically aligned with the valve handle"):
        robot.grab("valve handle")
    if check("the robot's gripper is forward aligned with valve handle and valve is horizontal"):
        robot.turn