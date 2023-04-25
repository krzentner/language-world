

if check("the robot's gripper is not above the plate"):
    robot.put("gripper above plate")
if check("the robot's gripper is above the plate and the robot's gripper is not horizontally aligned with the plate"):
    robot.align("gripper with plate")
if check("the robot's gripper is horizontally aligned with the plate and the robot's gripper is not near the plate"):
    robot.push("gripper into plate")
if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
    robot.slide("the plate to the goal")