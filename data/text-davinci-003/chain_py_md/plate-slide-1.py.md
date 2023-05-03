

Steps:
1. Put gripper above plate
2. Drop gripper around plate 
3. Slide plate to the goal

if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.close("gripper around plate")
if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.slide("the plate to the goal")