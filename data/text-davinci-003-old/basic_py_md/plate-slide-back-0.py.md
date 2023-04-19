

if check("the robot's gripper is not above the plate"):
    robot.put("gripper above plate")
if check("the plate is not aligned with the target location and the robot's gripper is not around the plate"):
    robot.grab("plate")
if check("the plate is aligned with the target location and the robot's gripper is not near the plate"):
    robot.slide("plate to goal")
if check("the robot's gripper is near the plate and the robot's gripper is open"):
    robot.drop("gripper around plate")
if check("the robot's gripper is around the plate and the plate is below the robot's gripper"):
    robot.slide("plate to goal")