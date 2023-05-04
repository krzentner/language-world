
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move("puck to goal")

# pick-place-wall: pick up the puck and hold it at the target location next to a wall
def pick_place_wall(robot):
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is not near puck and the robot's gripper is not around puck"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# pick-place-bin: pick up the puck and hold it at the target location in a bin
def pick_place_bin(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# pick-place-bin-wall: pick up the puck and hold it at the target location in a bin next to a wall
def pick_place_bin_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is not around puck and the robot