if check("the plate is not on the robot's gripper"):
        robot.grab("the plate")
    if check("the robot's gripper is not above the target location"):
        robot.move("the gripper above the target location")
    if check("the robot's gripper is above the target location and the plate is not near the target location"):
        robot.slide("the plate towards the target location")
    if check("the plate is near the target location"):
        robot.release("the plate at the target location")