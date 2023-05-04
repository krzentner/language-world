
    if check("the robot's gripper is not vertically aligned with ball"):
        robot.put("gripper above ball")
    if check("the robot's gripper is vertically aligned with ball"):
        robot.align("gripper with ball")
    if check("the robot's gripper is not around the ball and the robot's gripper is open"):
        robot.grab("ball")
    if check("the robot's gripper is above the ball"):
        robot.move("gripper above basketball hoop")
    if check("the robot's gripper is not above the hoop"):
        robot.place("gripper above basketball hoop")
    if check("the robot's gripper is not aligned with basket"):
        robot.move("gripper above hoop")
    if check("the ball is aligned with basket"):
        robot.drop("ball")

# valve-turn-cw: turn the valve clockwise
def valve_turn_cw(robot):
    if check("the robot's gripper is not vertically aligned with valve and the robot's gripper is open"):
        robot.align("gripper with valve")
    if check("the robot's gripper is vertically aligned with valve and the robot's gripper is open"):
        robot.grab("valve")
    if check("the robot's gripper is vertically aligned with valve"):
        robot.turn("valve clockwise")

# valve-turn-ccw: turn the valve counter clockwise
def valve_turn_ccw(robot):
    if check("the robot's gripper is not vertically aligned with valve and the robot's gripper is open"):
        robot.align("gripper with valve")
    if check("the robot's gripper is vertically aligned with valve and the robot's gripper is open"):
        robot.grab("valve")
    if check("the robot's gripper is vertically aligned with valve"):
        robot.turn("valve counter clockwise")

# button-press-side: push the button from the side
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is open"):
        robot.align("gripper with button")
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is open"):
        robot.grab("button")
    if check("the robot's gripper is vertically aligned