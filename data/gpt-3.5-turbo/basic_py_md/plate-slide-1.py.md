# plate-slide: slide the plate into the target location
def plate_slide(robot):
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    if check("the robot's gripper is above plate and the robot's gripper is closed"):
        if check("the plate is not aligned with the target"):
            robot.align("plate to target")
        if check("the plate is aligned with the target and the gripper is not at the target"):
            robot.move("gripper to target")
        if check("the gripper is above the target and the plate is aligned with the target"):
            robot.slide("plate to the goal")