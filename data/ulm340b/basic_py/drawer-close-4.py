
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.push("into drawer")

# window-close-side: slide the window closed by pressing from the side
def window_close_side(robot):
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

# door-close: push the door shut
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.push("door shut")

# door-lock: twist the door's knob to the locked position
def door_lock(robot):
    if check("the robot's gripper is not below door handle and the robot's gripper is not vertically aligned with door handle"):
        robot.move("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.turn("knob clockwise")

# pick-place-side: pick up the block and place it at the target location
def pick_place_side(robot):
    if check("the robot's gripper is not above block"):
        robot.move("gripper above block")
    if check("the robot's gripper is above block and the robot's gripper is not around