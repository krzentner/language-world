if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    if check("the robot's gripper is around the plate and the plate is not at the back position"):
        robot.slide("the plate to the back position")