
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("gripper above target")
    if check("the robot's gripper is not around target and the robot's gripper is open"):
        robot.drop("gripper around target")
    if check("the robot's gripper is near target and the robot's gripper is open"):
        robot.close("gripper around target")

# pick-place-wall: pick up the puck and move it to the target location
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# peg-unstack: pick the top peg up and drop it on the other peg
def peg_unstack(robot):
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.place("gripper above other peg")
    if check("the robot's gripper is above other peg and the robot's gripper is