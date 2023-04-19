

if check("the robot's gripper is not vertically aligned with the plate and the robot's gripper is not above the plate"):
    robot.put("gripper above plate")
if check("the robot's gripper is above the plate and the robot's gripper is not horizontally aligned with plate"):
    robot.align("gripper to plate")
if check("the robot's gripper is horizontally aligned with plate and the robot's gripper is not near plate"):
    robot.grab("plate")
if check("the robot's gripper is near plate and the plate is not near target"):
    robot.slide("plate to target")