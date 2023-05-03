if check("the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above the plate")
    if check("the robot's gripper is around the plate"):
        robot.release("the plate")
    if check("the plate is not at the back of the target location"):
        robot.move("the gripper to the back of the target location")
    if check("the robot's gripper is near the back of the target location and the plate is in front of the robot's gripper"):
        robot.slide("the plate sideways into the target location")