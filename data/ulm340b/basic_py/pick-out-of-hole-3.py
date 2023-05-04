
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.place("peg at goal")

# pick-place-wall: pick up the puck and hold it at the target location (the goal is against a wall)
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# pick-horizontal-wall: pick up the peg out of the hole in the wall
def pick_horizontal_wall(robot):
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.place("peg at goal")

# pick-vertical-wall: pick up the peg out of the hole in the wall
def pick_vertical_wall(robot):
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("g