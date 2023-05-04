
    if check("the robot's gripper is not around wrench"):
        robot.place("gripper around wrench")
    if check("the robot's gripper is around wrench and the robot's gripper is not horizontally aligned with peg"):
        robot.pull("wrench away from peg")
    if check("the robot's gripper is horizontally aligned with peg"):
        robot.place("wrench on peg")
    if check("the wrench is on the peg"):
        robot.move("gripper away")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not below door handle and the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper below door handle")
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.push("door closed")

# button-press-side: push the button from the side
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper in front of button")
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not near button"):
        robot.grab("button")
    if check("the robot's gripper is near button"):
        robot.push("down on button")

# door-unlock: pull the door handle up to unlock
def door_unlock(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.pull("up on door handle")

# door-lock: push the door handle down to lock
def door_lock(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with door handle"):