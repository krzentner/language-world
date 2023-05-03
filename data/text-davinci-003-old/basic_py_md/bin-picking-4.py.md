

if check("the robot's gripper is not above to the cube"):
    robot.put("gripper above cube")
if check("the robot's gripper is not around cube and the robot's gripper is open"):
    robot.close("gripper around cube")
if check("the robot's gripper is near the cube and the robot's gripper is closed"):
    robot.place("move the cube to the bin")
if check("the robot's gripper is near the bin and the cube is below the robot's gripper"):
    robot.drop("cube into the bin")