if check("the robot's gripper is not near the target location"):
        robot.move("gripper to target location")
    if check("the robot's gripper is near the target location"):
        robot.reach("gripper to target location")
    if check("the robot's gripper has reached the target location"):
        robot.grasp("target object")