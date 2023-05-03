

if check("the robot's gripper is not vertically aligned with the puck"):
    robot.put("gripper above puck")
if check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.drop("gripper around puck")
if check("the robot's gripper is near puck and the robot's gripper is closed"):
    robot.move("puck to goal")
if check("the robot's gripper is above puck and the robot's gripper is closed"):
    robot.lift("puck from the ground")
if check("the robot's gripper is moving forward and the puck is above the robot's gripper"):
    robot.move("gripper and puck to goal")