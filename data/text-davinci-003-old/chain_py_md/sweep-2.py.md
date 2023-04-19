

Steps:
1. Put gripper above cube
2. Grab cube with gripper
3. Move the cube sideways to goal

if check("the robot's gripper is not above cube"):
    robot.put("gripper above cube")
if check("the robot's gripper is above cube and the robot's gripper is open"):
    robot.grab("cube")
if check("the robot's gripper is above cube and the robot's gripper is closed"):
    robot.move("cube sideways to goal")