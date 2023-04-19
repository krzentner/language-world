

If check("the robot's gripper is not near cube"):
    robot.reach("to cube")
if check("the robot's gripper is not around cube and the robot's gripper is open"):
    robot.drop("gripper around cube")
if check("the robot's gripper is around cube and the robot's gripper is closed"):
    robot.move("gripper sideways to goal")
if check("the robot's gripper is near target"):
    robot.place("cube at goal")