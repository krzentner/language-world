
    if check("the robot's gripper is not vertically aligned with plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not forward aligned with plate"):
        robot.put("gripper in front of plate")
    if check("the robot's gripper is forward aligned with plate and the plate is not in goal"):
        robot.slide("plate in goal")

# lever-pull: pull the lever down
def lever_pull(robot):
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper around lever")
    if check("the robot's gripper is vertically aligned with lever"):
        robot.pull("down on lever")

# latch-turn-cw: turn the latch clockwise
def latch_turn_cw(robot):
    if check("the robot's gripper is not vertically aligned with latch"):
        robot.put("gripper above latch")
    if check("the robot's gripper is vertically aligned with latch and the robot's gripper is not around latch"):
        robot.put("gripper around latch")
    if check("the robot's gripper is forward aligned with latch and latch is not horizontal"):
        robot.turn("latch clockwise")

# latch-turn-ccw: turn the latch counterclockwise
def latch_turn_ccw(robot):
    if check("the robot's gripper is not vertically aligned with latch"):
        robot.put("gripper above latch")
    if check("the robot's gripper is vertically aligned with latch and the robot's gripper is not around latch"):
        robot.put("gripper around latch")
    if check("the robot's gripper is forward aligned with latch and latch is not horizontal"):
        robot.turn("latch counterclockwise")

# latch-close: close the latch
def latch_close(robot):
    if check("the robot's gripper is not above latch"):
        robot.put("gripper above latch")
    if check("the robot's gripper is forward aligned with latch and latch is not closed"):
        robot.close("latch")

# latch-open: open the latch
def latch_open(robot):
    if check("the robot's gripper is not above latch"):
        robot.put("gripper above latch")
    if check("the robot