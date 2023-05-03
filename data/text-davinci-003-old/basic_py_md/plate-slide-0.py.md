

if check("the robot's gripper is not above the plate"):
    robot.place("gripper above plate")
if check("the robot's gripper is above the plate and the robot's gripper is not forward of the plate"):
    robot.slide("gripper to forward of plate")
if check("the robot's gripper is forward of the plate"):
    robot.slide("plate to goal")