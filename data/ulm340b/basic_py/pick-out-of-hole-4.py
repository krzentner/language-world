
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg"):
        robot.pull("peg out of hole")
    if check("peg is out of hole"):
        robot.drop("peg at goal")

# pick-hollow-out-of-hole: pick up the hollow peg out of the hole and hold it at the target location
def pick_hollow_out_of_hole(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg"):
        robot.pull("peg out of hole")
    if check("peg is out of hole"):
        robot.drop("peg at goal")

# pick-place-wall: pick up the puck on the wall and hold it at the target location
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# pick-place-side: pick up the puck from the side and hold it at the target location
def pick_place_side(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper