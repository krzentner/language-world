
    if check("the robot's gripper is not vertically aligned with plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not near plate"):
        robot.push("gripper into plate")
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is near plate"):
        robot.slide("plate into goal")
    if check("the plate is in front of the robot's gripper"):
        robot.push("plate into goal harder")

# knob-turn-degrees-left: turn the knob left to a specified angle
def knob_turn_degrees_left(robot, d):
    if check("the robot's gripper is not vertically aligned with knob"):
        robot.put("gripper above knob")
    if check("the robot's gripper is vertically aligned with knob"):
        robot.grab("knob")
    if check("the robot's gripper is around knob"):
        robot.rotate("knob left to " + d)

# knob-turn-degrees-right: turn the knob right to a specified angle
def knob_turn_degrees_right(robot, d):
    if check("the robot's gripper is not vertically aligned with knob"):
        robot.put("gripper above knob")
    if check("the robot's gripper is vertically aligned with knob"):
        robot.grab("knob")
    if check("the robot's gripper is around knob"):
        robot.rotate("knob right to " + d)

# knob-turn-left: turn the knob left until it stops
def knob_turn_left(robot):
    if check("the robot's gripper is not vertically aligned with knob"):
        robot.put("gripper above knob")
    if check("the robot's gripper is vertically aligned with knob and the robot's gripper is not left of knob"):
        robot.grab("knob")
    if check("the robot's gripper is left of knob"):
        robot.rotate("knob left")
    if check("the robot's gripper is in front of knob"):
        robot.rotate("knob left harder")

# knob-turn-right: turn the knob right until it stops
def knob_turn_right(robot):
    if check("the robot's gripper is not vertically aligned with knob"):
        robot