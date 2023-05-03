if check("the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around the plate"):
        robot.grab("the plate")
    if check("the robot's gripper is around the plate and the plate is not on the target location"):
        robot.slide("the plate to the target location")
    if check("the plate is on the target location and the robot's gripper is around the plate"):
        robot.release("the plate")