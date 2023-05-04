
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is below the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not near the button"):
        robot.reach("over the short wall and touch button")
    if check("the robot's gripper is near button"):
        robot.push("down on button")

# pick-place-wall: pick up the puck and place it in the target location, with a tall wall in between
def pick_place_wall(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is not near puck"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is not closed and the robot's gripper is near puck"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.hold("puck over wall")
    if check("the robot's gripper is not near goal"):
        robot.place("puck at goal")

# pick-out-of-hole: pick up the peg from inside the hole
def pick_out_of_hole(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.pull("peg out of hole")

# pick-out-of-hole-side: pick up the peg from inside the hole, starting from the side
def pick_out_of_hole_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
  