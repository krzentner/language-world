

if check("the robot's gripper is not vertically aligned with the plate"):
    robot.put("gripper at the side of the plate")
if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with the target location"):
    robot.align("plate horizontally with target location")
if check("the plate is horizontally aligned with target location"):
    robot.slide("plate back sideways")