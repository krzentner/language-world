
    if check("the robot's gripper is not above plate and the robot's gripper is not vertically aligned with the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near plate"):
        robot.grab("gripper around the plate")
    if check("the robot's gripper is near the plate and the plate is not horizontally aligned with target"):
        robot.align("plate to target")
    if check("the plate is horizontally aligned with target"):
        robot.slide("plate to the side until it reaches target")