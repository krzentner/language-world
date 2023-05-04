
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is above the plate and the robot's gripper is not touching the plate"):
        robot.push("gripper towards the plate")
    if check("the robot's gripper is touching the plate"):
        robot.push("plate towards goal")

# peg-insert-topdown: grab the peg and insert it into the hole from top-down
def peg_insert_topdown(robot):
    if check("the robot's gripper is not above peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is above peg and the robot's gripper is not touching the peg"):
        robot.push("gripper towards the peg")
    if check("the robot's gripper is touching the peg"):
        robot.grab("peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# door-close: push the door close
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.push("door closed")

# plate-slide-topdown: slide the plate forwards into the target location
def plate_slide_topdown(robot):
    if check("the robot's gripper is not above plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is above the plate and the robot's gripper is not touching the plate"):
        robot.push("gripper towards the plate")
    if check("the robot's gripper is touching the plate"):
        robot.push("plate towards goal")