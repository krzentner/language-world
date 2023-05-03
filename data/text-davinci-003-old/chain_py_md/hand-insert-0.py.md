

Steps:
  1. Put gripper above puck
  2. Drop gripper around puck
  3. Close gripper around puck
  4. Move puck sideways toward goal

if check("the robot's gripper is not above puck"):
    robot.put("gripper above puck")
if check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.drop("gripper around puck")
if check("the robot's gripper is near puck and the robot's gripper is open"):
    robot.close("gripper around puck")
if check("the robot's gripper is above puck and the robot's gripper is closed"):
    robot.move("sideways toward goal")