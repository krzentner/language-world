if check("the plate is not in the robot's gripper and the gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the gripper is above the plate and the gripper is not closed"):
        robot.close("gripper around plate")
    if check("the gripper is above the plate and the plate is inside the gripper"):
        robot.slide("plate to goal location")