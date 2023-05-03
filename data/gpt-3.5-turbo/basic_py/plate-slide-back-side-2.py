if check("the robot's gripper is not horizontally aligned with the plate"):
    robot.align("gripper to plate")
if check("the plate is not to the left of the robot's gripper"):
    robot.move("gripper to left of plate")
if check("the robot's gripper is near the plate and the robot's gripper is open"):
    robot.close("gripper around plate")
if check("the plate is between the robot's gripper and the target location"):
    robot.slide("plate to the left")
if check("the plate is at the target location"):
    robot.drop("plate at goal")