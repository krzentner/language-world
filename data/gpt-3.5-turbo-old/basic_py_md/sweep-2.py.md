# sweep: grab the cube and move sideways it to the target location
# def sweep(robot):
if check("the robot's gripper is not above cube"):
    robot.place("the gripper above cube")
if check("the robot's gripper is not around cube and the robot's gripper is open"):
    robot.drop("the gripper around cube")
if check("the robot's gripper is near cube and the robot's gripper is open"):
    robot.close("the gripper around cube")
if check("the robot's gripper is holding cube and the robot is not near target"):
    robot.move("to the side")
if check("the robot is at the target location"):
    robot.drop("cube")