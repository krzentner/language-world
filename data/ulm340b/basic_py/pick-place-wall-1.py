
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("gripper over goal")

# pick-place-wall-high: pick up the puck and hold it at the target location with a tall wall in the way
def pick_place_wall_high(robot):
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is closed"):
        robot.move("to the goal")

# pick-place-v2: pick up the puck and hold it at the target location
def pick_place_v2(robot):
    if check("the robot's gripper is not vertically aligned with puck and the robot's gripper is not below puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above the puck and the robot's gripper is not around puck"):
        robot.grab("puck")
    if check("the robot's gripper is around puck and the robot's gripper is above puck"):
        robot.move("to goal")

# pick-place-easy: pick up the puck and hold it at the target location, easier version
def pick_place_easy(robot):
    if check("the robot's gripper is not vertically aligned with puck and the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.grab("puck")
 