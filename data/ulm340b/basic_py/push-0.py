
    if check("the robot's gripper is not horizontally aligned with puck"):
        robot.move("gripper to side of puck")
    if check("the robot's gripper is forward aligned with puck and the robot's gripper is not left of the puck"):
        robot.push("puck forward")
    if check("the puck is near goal"):
        robot.push("puck into goal")

# pick-place-wall: pick up the puck and hold it at the target location next to the wall
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck near wall")

# pick-wall: pick the puck near the wall
def pick_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")

# pick-place-table: pick up the puck and hold it at the target location on the table
def pick_place_table(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck on table")

# pick-place-bin: pick