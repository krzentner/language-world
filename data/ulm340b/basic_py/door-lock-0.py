
    if check("the robot's gripper is not near lock dial"):
        robot.move("gripper to left of dial")
    if check("the robot's gripper is near lock dial"):
        robot.grasp("dial")
    if check("the robot's gripper is forward aligned with dial"):
        robot.turn("left")

# turn-dial: turn the dial
def turn_dial(robot):
    if check("the robot's gripper is not near dial"):
        robot.move("gripper to left of dial")
    if check("the robot's gripper is near dial"):
        robot.grab("dial")
    if check("the robot's gripper is forward aligned with dial"):
        robot.turn("left")

# turn-dial-full-circle: turn the dial clockwise one revolution
def turn_dial_full_circle(robot):
    if check("the robot's gripper is not near dial"):
        robot.move("gripper to left of dial")
    if check("the robot's gripper is near dial"):
        robot.grab("dial")
    if check("the robot's gripper is forward aligned with dial"):
        robot.turn("left 360 degrees")

# turn-valve: turn the valve
def turn_valve(robot):
    if check("the robot's gripper is not near valve"):
        robot.move("gripper to left of valve")
    if check("the robot's gripper is near valve"):
        robot.grasp("valve")
    if check("the robot's gripper is forward aligned with valve"):
        robot.turn("left")

# latch: flip the latch
def latch(robot):
    if check("the robot's gripper is not near latch"):
        robot.put("gripper to the right of latch")
    if check("the robot's gripper is near latch"):
        robot.grasp("latch")
    if check("the robot's gripper is forward aligned with latch"):
        robot.push("latch up")

# knob-open: turn the knob counterclockwise
def knob_open(robot):
    if check("the robot's gripper is not near knob"):
        robot.move("gripper to left of knob")
    if check("the robot's gripper is near knob"):
        robot.grasp("knob")