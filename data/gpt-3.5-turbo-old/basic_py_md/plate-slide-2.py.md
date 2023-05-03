# plate-slide: slide the plate into the target location
# def plate_slide(robot):
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    if check("the robot's gripper is far from the goal and the plate is between the robot's gripper and the goal"):
        robot.slide("plate towards the goal")
    if check("the robot's gripper is near the goal and the plate is below the robot's gripper"):
        robot.slide("plate into the goal")