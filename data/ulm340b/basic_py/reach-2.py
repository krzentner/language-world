
    if check("the robot's gripper is not above the goal"):
        robot.place("gripper above goal")
    if check("the robot's gripper is above the goal"):
        robot.move("gripper to goal")

# pick-place-wall: pick up the puck and hold it at the target location
def pick_place_wall(robot):
    if check("the robot's gripper is not in front of the goal"):
        robot.align("gripper to goal")
    if check("the robot's gripper is in front of the goal"):
        robot.move("gripper to goal")
    if check("the robot's gripper is in front of the goal"):
        robot.grab("the goal")
    if check("the robot's gripper is above the goal and the robot's gripper is closed"):
        robot.place("puck at goal")

# pick-place-back: pick up the puck and hold it at the target location
def pick_place_back(robot):
    if check("the robot's gripper is not in front of the goal"):
        robot.align("gripper to goal")
    if check("the robot's gripper is in front of the goal"):
        robot.grab("goal")
    if check("the robot's gripper is in front of the goal"):
        robot.move("gripper to goal")
    if check("the robot's gripper is above the goal and the robot's gripper is closed"):
        robot.place("puck at goal")

# pick-place-left: pick up the puck and hold it at the target location
def pick_place_left(robot):
    if check("the robot's gripper is not in front of the goal"):
        robot.align("gripper to goal")
    if check("the robot's gripper is in front of the goal"):
        robot.grab("goal")
    if check("the robot's gripper is in front of the goal"):
        robot.move("gripper to goal")
    if check("the robot's gripper is above the goal and the robot's gripper is closed"):
        robot.place("puck at goal")

# pick-place-right: pick up the puck and hold it at the target location
def pick_place_right(robot):
    if check("the robot's gripper is not in front of the