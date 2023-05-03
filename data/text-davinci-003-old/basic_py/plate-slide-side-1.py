
    if check("the robot's gripper is not above plate"):
        robot.place("gripper above plate")
    if check("the robot's gripper is forward aligned with the plate and the robot's gripper is not in front of plate edge and the robot's gripper is not below plate"):
        robot.lift("plate slightly")
    if check("the robot's gripper is in front of plate edge and the robot's gripper is below plate and the plate is not left of robot's gripper"):
        robot.slide("plate left")
    if check("the plate is left of the robot's gripper"):
        robot.release("plate at goal")