
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is above handle and handle is not left of the robot's gripper"):
        robot.grab("handle")
    if check("the robot's gripper is forward aligned with handle"):
        robot.pull("handle up")

# handle-pull: pull up the handle
def handle_pull(robot):
    if check("the robot's gripper is not almost vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is above handle and handle is not left of the robot's gripper"):
        robot.grab("handle")
    if check("the robot's gripper is forward aligned with handle"):
        robot.pull("handle up")

# knob-turn-count: turn the knob a specific amount clockwise or counter-clockwise
def knob_turn_count(robot):
    if check("the robot's gripper is not vertically aligned with knob and the robot's gripper is not right of knob"):
        robot.put("gripper above knob")
    if check("the robot's gripper is above knob and the robot's gripper is not around knob"):
        robot.grab("knob")
    if check("the robot's gripper is around knob"):
        robot.turn("knob")

# knob-turn: turn the knob until it doesn't turn any more
def knob_turn(robot):
    if check("the robot's gripper is not vertically aligned with knob and the robot's gripper is not right of knob"):
        robot.put("gripper above knob")
    if check("the robot's gripper is above knob and the robot's gripper is not around knob"):
        robot.grab("knob")
    if check("the robot's gripper is around knob"):
        robot.turn("knob")

# pick-place-simple: pick up the block and hold it at the target location
def pick_place_simple(robot):
    if check("the robot's gripper is not vertically aligned with block"):
        robot.put("gripper above block")
    if check("the robot's gripper is vertically aligned with block and the robot's gripper is not around block"):
        robot.drop("gripper around block")
    if check("the robot'