

If check("the robot's gripper is not near the plate"):
    robot.move("gripper to left of the plate")
if check("the robot's gripper is near the plate"):
    robot.grab("plate")
if check("the robot's gripper is holding the plate and the plate is not horizontally aligned with the goal"):
    robot.align("plate with goal")
if check("the plate is horizontally aligned with the goal"):
    robot.slide("plate back")