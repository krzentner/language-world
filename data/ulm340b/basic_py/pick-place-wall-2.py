
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around puck"):
        robot.lift("puck up")
    if check("the robot's gripper is above the puck"):
        robot.place("puck over wall")

# pick-place-high: pick up the puck and hold it at the target location which is above the target
def pick_place_high(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around puck"):
        robot.lift("puck high")
    if check("the robot's gripper is above the puck"):
        robot.place("puck over wall")
    if check("puck is above the goal"):
        robot.drop("puck onto goal")

# pick-place-back: pick up the puck and hold it at the target location on the other side of the puck
def pick_place_back(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around puck"):
        robot.lift("puck up")
    if check("the robot's gripper is above the puck"):
        robot.place("puck behind")

# pick-insert-side: grab the puck and insert it into the slot from the side
def pick_insert_side(robot):
    if check("