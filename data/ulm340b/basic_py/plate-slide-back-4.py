
    if check("the robot's gripper is not above plate"):
        robot.place("gripper above plate")
    if check("the robot's gripper is not vertically aligned with plate and the robot's gripper is not near the plate"):
        robot.push("gripper into plate")
    if check("the robot's gripper is near plate"):
        robot.slide("plate to goal")

# slide-back-side: slide the puck to the target location along the side
def slide_back_side(robot):
    if check("the robot's gripper is not above the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is in front of the robot's gripper"):
        robot.slide("the puck to the goal")

# drawer-close-side: push the drawer close from the side
def drawer_close_side(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.push("drawer closed")

# peg-insert-side-v2: grab the peg and insert it into the hole from the side
def peg_insert_side_v2(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# plate-slide-forward: slide the plate forward to the target location
def plate_slide_forward(robot):
    if check("the robot's gripper is not above plate"):
        robot.