

if check("the robot's gripper is not vertically aligned with the plate and the robot's gripper is below the plate"):
    robot.put("gripper above plate")
if check("the robot's gripper is vertically aligned with the plate and the plate is not left of the robot's gripper"):
    robot.grab("plate")
if check("the robot's gripper is near right of the plate and the plate is not horizontally aligned with goal"):
    robot.align("plate to goal")
if check("the robot's gripper is near left of the plate and the plate is horizontally aligned with goal"):
    robot.slide("plate left into goal")