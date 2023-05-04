
    if check("the hammer is not above the nail and the hammer is not vertically aligned with the nail"):
        robot.place("hammer above nail")
    if check("the hammer is vertically aligned with the nail"):
        robot.push("hammer down onto nail")

# door-lock: turn the door lock clockwise
def door_lock(robot):
    if check("the door lock is not near the robot's gripper"):
        robot.move("the gripper towards the door lock")
    if check("the robot's gripper is below the door lock"):
        robot.turn("the door lock clockwise")

# knob-turn-counter-clockwise-left: turn the left door knob counter-clockwise
def knob_turn_counter_clockwise_left(robot):
    if check("the robot's gripper is not above the left door knob"):
        robot.place("the gripper above the left door knob")
    if check("the robot's gripper is below the left door knob"):
        robot.turn("the left door knob counter-clockwise")

# knob-turn-counter-clockwise-right: turn the right door knob counter-clockwise
def knob_turn_counter_clockwise_right(robot):
    if check("the robot's gripper is not above the right door knob"):
        robot.place("the gripper above the right door knob")
    if check("the robot's gripper is below the right door knob"):
        robot.turn("the right door knob counter-clockwise")

# knob-turn-clockwise-left: turn the left door knob clockwise
def knob_turn_clockwise_left(robot):
    if check("the robot's gripper is not above the left door knob"):
        robot.place("the gripper above the left door knob")
    if check("the robot's gripper is below the left door knob"):
        robot.turn("the left door knob clockwise")

# knob-turn-clockwise-right: turn the right door knob clockwise
def knob_turn_clockwise_right(robot):
    if check("the robot's gripper is not above the right door knob"):
        robot.place("the gripper above the right door knob")
    if check("the robot's gripper is below the right door knob"):
        robot.turn("the right door knob clockwise")

# turn-off: rotate the dial clockwise
def turn_off(robot):
    if check("the robot's gripper is not above the dial and