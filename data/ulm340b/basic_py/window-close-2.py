
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is right of the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is in front of the window handle"):
        robot.slide("window right")

# peg-insert-side-limited: grab the peg and insert it into the hole from the side
def peg_insert_side_limited(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# door-open-limited: pull the door open
def door_open_limited(robot):
    if check("the robot's gripper is not vertically aligned with door handle and the robot's gripper is not forward aligned with door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with the door handle and the door is not open"):
        robot.pull("door open")

# drawer-close-limited: push the drawer closed
def drawer_close_limited(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle and the robot's gripper is not forward aligned with drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# pick-place-limited: pick up the puck and hold it at the target location
def pick_place_limited(robot):
    if check("the robot's gripper is not above the puck and the robot's gripper is not around the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is closed"):