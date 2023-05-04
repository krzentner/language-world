
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.pull("away from door")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# lever-pull: pull the lever left
def lever_pull(robot):
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is vertically aligned with lever and the robot's gripper is not around lever"):
        robot.grab("lever")
    if check("the robot's gripper is around lever and the robot's gripper is forward aligned with lever"):
        robot.pull("left")
    if check("the robot's gripper is around lever and the robot's gripper is near lever"):
        robot.move("left")

# knob-turn-clockwise: turn the knob clockwise
def knob_turn_clockwise(robot):
    if check("the robot's gripper is not vertically aligned with knob and the robot's gripper is not around knob"):
        robot.put("gripper above knob")
    if check("the robot's gripper is vertically aligned with knob and the robot's gripper is not around knob"):
        robot.put("gripper around knob")
    if check("the robot's gripper is around knob and the robot's gripper is not forward aligned with knob"):
        robot.grab("knob")
    if check("the robot's gripper is around knob and the robot's gripper is forward aligned with knob"):
        robot.twist("knob")

# knob-turn-counterclockwise: turn the knob counterclockwise
def knob_turn_counterclockwise(robot):
    if check("the robot's gripper is not vertically aligned with knob and the robot's gripper is not around knob"):
        robot.put("gripper