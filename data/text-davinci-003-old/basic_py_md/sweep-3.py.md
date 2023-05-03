

if check("the robot's gripper is not above the cube"):
    robot.place("gripper above cube")
if check("the robot's gripper is not around the cube and the gripper is open"):
    robot.drop("gripper around cube")
if check("the robot's gripper is near the cube and the gripper is open"):
    robot.close("gripper around cube")
if check("the robot's gripper is near the cube and the cube is below the gripper"):
    robot.slide("cube to goal")