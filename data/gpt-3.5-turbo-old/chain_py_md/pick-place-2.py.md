# pick-place: pick up the puck and hold it at the target location
# def pick_place(robot):
# Steps:
#  1. Put gripper above puck
#  2. Drop gripper around puck
#  3. Close gripper around puck
#  4. Move puck to goal

if check("the robot's gripper is not above the puck"):
    robot.place("gripper above puck")

if check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.drop("gripper around puck")
    
if check("the robot's gripper is near puck and the robot's gripper is open"):
    robot.close("gripper around puck")

if check("the robot's gripper is above puck and the robot's gripper is closed"):
    robot.reach("to goal")