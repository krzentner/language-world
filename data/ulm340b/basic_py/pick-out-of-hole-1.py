
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is above peg and the robot's gripper is not vertically aligned with peg"):
        robot.move("gripper onto peg")
    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is not around peg"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is around peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.pull("peg out of hole")
    if check("the robot's gripper is above the peg"):
        robot.place("peg at goal")

# pick-horizontal: pick up the puck horizontally and place it in the target location
def pick_horizontal(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is not horizontally aligned with puck"):
        robot.move("gripper to left of puck")
    if check("the robot's gripper is horizontally aligned with puck and the robot's gripper is not around puck"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is closed"):
        robot.lift("puck out of hole")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# stack: place the puck into the other puck
def stack(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is not vertically aligned with puck"):
        robot.move("gripper onto puck")
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is not around puck"):