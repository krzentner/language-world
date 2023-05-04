
    if check("the robot's gripper is not above the button"):
        robot.place("gripper above button")
    if check("the robot's gripper is above button"):
        robot.press("the button")

# pick-place-wall: pick up the puck and hold it at the target location with the wall to the left of the robot
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.place("gripper around puck")
    if check("the robot's gripper is above puck"):
        robot.place("puck at goal")

# peg-unplug-side: grab the peg and remove it from the hole from the side
def peg_unplug_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not forward aligned with the robot's gripper and peg is not horizontally aligned with hole"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.move("peg out of hole")
    if check("peg is horizontally aligned with hole"):
        robot.remove("peg from hole")

# pick-place-wall-behind: pick up the puck and hold it at the target location with the wall behind the robot
def pick_place_wall_behind(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not above puck and the robot's gripper is open"):
        robot.place("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.place("gripper around puck")
    if check("the robot's gripper is around puck"):
        robot.place("puck at goal")

# peg-unplug-topdown: grab the peg and remove it from the hole from above
def peg_unplug_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot