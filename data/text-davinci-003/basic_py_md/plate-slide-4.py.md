

if check("the robot's gripper is not above the plate"):
    robot.put("gripper above plate")
if check("the robot's gripper is above the plate and the robot's gripper is not open"):
        robot.open("gripper around plate")
if check("the robot's gripper is above plate and the robot's gripper is open"):
        robot.pull("plate to goal")
if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.slide("plate to goal")