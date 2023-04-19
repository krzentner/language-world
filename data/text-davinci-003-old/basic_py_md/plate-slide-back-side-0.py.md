

if check("the robot's gripper is not forward aligned with the plate"):
    robot.put("gripper above plate")
if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with the target location"):
    robot.grab("plate")
if check("the robot's gripper is not forward aligned with the plate and the plate is horizontally aligned with the target location"):
    robot.slide("plate back sideways")
if check("the robot's gripper is forward aligned with the plate and the plate is not near the target location"):
    robot.push("plate back into target location")