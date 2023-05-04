
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")

# knob-turn-ccw: turn the doorknob counterclockwise
def knob_turn_ccw(robot):
    if check("the robot's gripper is not above the door knob"):
        robot.place("gripper above door knob")
    if check("the robot's gripper is above the door knob and the robot's gripper is open"):
        robot.close("gripper around door knob")
    if check("the robot's gripper is around the door knob"):
        robot.rotate("knob ccw")

# knob-turn-cw: turn the doorknob clockwise
def knob_turn_cw(robot):
    if check("the robot's gripper is not above the door knob"):
        robot.place("gripper above door knob")
    if check("the robot's gripper is above the door knob and the robot's gripper is open"):
        robot.close("gripper around door knob")
    if check("the robot's gripper is around the door knob"):
        robot.rotate("knob cw")

# lever-pull: pull the lever
def lever_pull(robot):
    if check("the robot's gripper is not near lever"):
        robot.grab("lever")
    if check("the robot's gripper is near lever and the robot's gripper is not around lever"):
        robot.wrap("hand around lever")
    if check("the robot's gripper is around lever"):
        robot.pull("lever")

# handle-pull: pull the handle
def handle_pull(robot):
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is above handle and the robot's gripper is not around handle"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is around handle"):
        robot.pull("handle")

# hook-move: move