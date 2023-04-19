
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is above the plate and the robot's gripper is not near the plate and the plate is right of the robot's gripper"):
        robot.slide("plate antisunwise")
    if check("the robot's gripper is above the plate and the robot's gripper is not near the plate and the plate is not right of the robot's gripper"):
        robot.slide("plate sunwise")
    if check("the robot's gripper is near the plate and the plate is left of the robot"):
        robot.slide("plate to goal")