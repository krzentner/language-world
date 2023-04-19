

Then, provide the following steps:

1. Put gripper above plate
2. Drop gripper around plate
3. Slide plate to goal

if check("the robot's gripper is not above plate"):
    robot.put("gripper above plate")
if check("the robot's gripper is not around plate and the robot's gripper is open"):
    robot.drop("gripper around plate")
if check("the robot's gripper is around plate"):
    robot.slide("plate to goal")