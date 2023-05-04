
    if check("the robot's gripper is not almost vertically aligned with cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is almost vertically aligned with cube and the robot's gripper is not around cube"):
        robot.put("gripper around cube")
    if check("the robot's gripper is around cube"):
        robot.sweep("cube to the goal")
    if check("the robot's gripper is horizontally aligned with cube"):
        robot.drop("cube at goal")

# pick-place-wall: pick the puck from the wall and place it on the shelf
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# stack: pick the puck from the table and place it on the cube
def stack(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck on cube")

# pick-out-of-hole: pick the peg out of the hole
def pick_out_of_hole(robot):
    if check("the robot's gripper is not near peg"):
        robot.put("gripper near peg")
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is near peg and the robot's grip