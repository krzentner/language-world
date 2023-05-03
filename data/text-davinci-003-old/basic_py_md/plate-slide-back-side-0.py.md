

if check("the robot's gripper is not above the plate"):
    robot.put("gripper above plate")
if check("the robot's gripper is above the plate and the gripper is not around the plate"):
    robot.drop("gripper around plate")
if check("the robot's gripper is around plate and plate is not facing the destination"):
    robot.rotate("plate towards destination")
if check("plate is facing the destination and the robot's gripper is in front of the plate"):
    robot.push("plate sideways to the destination")