if check("the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around plate"):
        robot.grab("the plate")
    if check("the robot's gripper is around the plate and the plate is not in the target location"):
        robot.slide("the plate to the target location")
    if check("the plate is in the target location"):
        robot.release("the plate")