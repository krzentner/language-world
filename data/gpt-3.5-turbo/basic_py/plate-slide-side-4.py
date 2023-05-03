if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    if check("the robot's gripper is almost vertically aligned with the target location and the plate is not yet at the target location"):
        robot.slide("the plate sideways towards the target location")
    if check("the plate is at the target location"):
        robot.release("gripper around plate")