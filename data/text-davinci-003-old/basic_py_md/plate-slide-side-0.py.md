

if check("the robot's gripper is not vertically aligned with the plate"):
    robot.put("gripper above plate")
if check("the plate is not left of the robot's gripper and the plate is not forward aligned with the robot's gripper"):
    robot.grab("plate")
if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with the target"):
    robot.align("plate to target")
if check("the plate is horizontally aligned with the target"):
    robot.slide("plate to the target")