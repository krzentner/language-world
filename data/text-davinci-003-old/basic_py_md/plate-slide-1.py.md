

if check("the robot’s gripper is not in range with the plate"):
    robot.move("gripper above plate")
if check("the robot’s gripper is in range with the plate and the robot’s gripper is not near the plate"):
    robot.push("gripper into the plate")
if check("the robot’s gripper is near the plate and the plate is below the robot’s gripper"):
    robot.slide("the plate to the goal")