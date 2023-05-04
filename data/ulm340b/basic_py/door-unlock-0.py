
    if check("the dial handle is not left of the robot's gripper and the dial handle is not almost vertically aligned with the robot's gripper"):
        robot.move("the gripper next to the dial handle")
    if check("the robot's gripper is around the dial handle and the robot's gripper is open"):
        robot.grab("dial handle")
    if check("the robot's gripper is forward aligned with the dial handle"):
        robot.turn("dial")

# pick: pick up the puck
def pick(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is open"):
        robot.grab("puck")

# pick-place-wall: pick up the puck and place it at the target location
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# peg-insert: grab the peg and insert it into the hole
def peg_insert(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not aligned with hole"):
        robot.align("peg to hole")
    if check("peg is aligned with hole"):
        robot.insert("peg into hole")

# turn-and-open: turn the dial on the door and pull the door open
def turn_and_open(robot):
    if check("the dial handle is not left of the robot's gripper and the dial handle is not