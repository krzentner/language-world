
    if check("the robot's gripper is not near button and the robot's gripper is not forward aligned with button"):
        robot.move("gripper to front of button")
    if check("the robot's gripper is forward aligned with the button and the robot's gripper is not near button"):
        robot.push("gripper into button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.press("button")

# pick-and-place-wall: pick up the puck and hold it near the target wall location
def pick_and_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# peg-insert-side-v2: grab the peg and insert it into the hole from the side
def peg_insert_side_v2(robot):
    if check("the robot's gripper is not above peg"):
        robot.place("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# drawer-open-v2: pull the drawer open
def drawer_open_v2(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away