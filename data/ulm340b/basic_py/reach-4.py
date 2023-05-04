
    if check("the robot's gripper is not vertically aligned with the goal"):
        robot.put("gripper above goal")

# slide: slide the puck to the target location
def slide(robot):
    if check("the robot's gripper is above puck and the puck is not horizontally aligned with goal"):
        robot.move("gripper to below puck")
    if check("the robot's gripper is near puck"):
        robot.slide("the puck to the goal")
    if check("the robot's gripper is in front of the puck"):
        robot.push("the puck towards the goal harder")

# pick-place-wall: pick up the puck, pull it past the wall, and hold it at the target location
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move("gripper to above wall")
    if check("the robot's gripper is above the wall"):
        robot.place("gripper above the goal")

# pick-place-wall-v1: pick up the puck, pull it over the wall, and hold it at the target location
def pick_place_wall_v1(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move("gripper to above wall")
    if check("the robot's gripper is above the wall"):
        robot.place("gripper above the goal")

# pull-wall-v1: