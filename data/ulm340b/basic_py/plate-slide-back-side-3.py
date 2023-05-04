
    if check("the robot's gripper is not vertically aligned with the plate handle and the plate handle is not above the robot's gripper"):
        robot.put("gripper above plate handle")
    if check("the robot's gripper is vertically aligned with plate handle and the robot's gripper is not near the plate handle"):
        robot.push("into plate handle")
    if check("the robot's gripper is near the plate handle"):
        robot.slide("plate back and to the left")
    if check("the robot's gripper is in front of the plate handle"):
        robot.push("plate harder")

# plate-slide-back: slide the plate backwards into the target location
def plate_slide_back(robot):
    if check("the robot's gripper is not vertically aligned with the plate handle and the plate handle is not above the robot's gripper"):
        robot.put("gripper above plate handle")
    if check("the robot's gripper is vertically aligned with plate handle and the robot's gripper is not near the plate handle"):
        robot.push("into plate handle")
    if check("the robot's gripper is near the plate handle"):
        robot.slide("plate back")
    if check("the robot's gripper is in front of the plate handle"):
        robot.push("plate harder")

# knob-turn-pull: grasp the knob, pull it out, and turn it to the target rotation
def knob_turn_pull(robot):
    if check("the robot's gripper is not vertically aligned with the knob"):
        robot.put("gripper above knob")
    if check("the robot's gripper is vertically aligned with knob and the knob is not around the robot's gripper"):
        robot.put("gripper around knob")
    if check("the robot's gripper is around knob"):
        robot.pull("knob out")
    if check("the robot's gripper is around knob and the knob is not aligned vertically with the left of the goal"):
        robot.turn("knob left")

# knob-turn-push: grasp the knob, push it in, and turn it to the target rotation
def knob_turn_push(robot):
    if check("the robot's gripper is not vertically aligned with the knob"):
        robot.put("gripper above knob")
    if check("the robot's gripper is vertically aligned with knob and the knob