
    if check("the robot's gripper is not above plate"):
        robot.place("gripper above plate")
    if check("the plate is not backwards aligned with the robot's gripper"):
        robot.align("plate backwards")
    if check("the plate is above the target location and the robot's gripper is above the plate"):
        robot.slide("plate back")