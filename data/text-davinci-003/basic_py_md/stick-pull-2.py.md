

if check("the robot's gripper is not vertically aligned with the stick"):
    robot.place("gripper above stick")
if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not near stick"):
    robot.grab("stick")
if check("the robot's gripper is near the stick and the thermometer is below the stick"):
    robot.pull("stick to the goal")