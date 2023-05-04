
    if check("the robot's gripper is not above door handle"):
        robot.place("gripper above door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.pull("door open")

# valve-open: turn the valve
def valve_open(robot):
    if check("the robot's gripper is not vertically aligned with valve"):
        robot.put("gripper above valve")
    if check("the robot's gripper is vertically aligned with the valve"):
        robot.turn("valve to the right")

# valve-turn: turn the valve
def valve_turn(robot):
    if check("the robot's gripper is not above valve"):
        robot.place("gripper above valve")
    if check("the robot's gripper is vertically aligned with the valve"):
        robot.turn("valve")

# door-unlock: turn the dial on the door
def door_unlock(robot):
    if check("the robot's gripper is not above door handle"):
        robot.place("gripper above door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.pull("door open")

# button-press-bottomup: push the button up from the side
def button_press_bottomup(robot):
    if check("the robot's gripper is not right of button"):
        robot.move("gripper to right of button")
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("up on button")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not above door handle"):
        robot.place("gripper above door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not around door handle"):