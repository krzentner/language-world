

If check("the robot's gripper is not above plate and the robot's gripper is not vertically aligned with plate"):
    robot.put("the gripper above the plate")
if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near plate"):
    robot.push("the gripper into the plate")
if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
    robot.slide("the plate to the goal")