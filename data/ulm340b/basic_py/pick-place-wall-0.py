
    if check("the robot's gripper is not above the puck"):
        robot.move("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# pick-place-bin: pick up the puck and hold it at the target location, with a bin around the puck
def pick_place_bin(robot):
    if check("the robot's gripper is not above the puck"):
        robot.move("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# pick-place-bin-above: pick up the puck and hold it at the target location, with a bin around the puck, from above
def pick_place_bin_above(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# pick-place-bin-above-short: pick up the puck and hold it at the target location, with a short bin around the puck, from above
def pick_place_bin_above_short(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
