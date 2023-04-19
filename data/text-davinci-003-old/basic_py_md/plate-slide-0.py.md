

if check("the robot's gripper is not near the plate and the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is above plate and the robot's gripper is not around plate"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is around the plate and the plate is not at the target location"):
        robot.slide("plate to goal")
    if check("the robot's gripper is near the plate and the plate is at the target location"):
        robot.release("gripper from plate")