if check("the robot's gripper is not above the target location"):
        robot.move("the gripper to the target location")
    if check("the robot's gripper is above the target location"):
        robot.grab("the object at the target location")