
    if check("the robot's gripper is not above the wall and not vertically aligned with the wall"):
        robot.place("gripper above wall")
    if check("the robot's gripper is vertically aligned with the wall and not over the wall"):
        robot.put("gripper over the wall")
    if check("the robot's gripper is vertically aligned with the wall and over the wall"):
        robot.move("gripper to goal")

# pick: pick up the puck
def pick(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.pick("puck up")

# place: place the puck at the target location
def place(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# stack: place the blue puck on top of the red puck
def stack(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.lift("puck up")
    if check("the robot's gripper is above puck and the puck is above another puck"):
        robot.drop("the puck on top of the other puck")

# pick-place-wall: pick up the puck and place it over a wall at the target location
def pick_place_wall(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.close("gripper around puck")
  