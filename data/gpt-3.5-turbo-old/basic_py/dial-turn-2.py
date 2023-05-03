if check("the robot's gripper is not around the dial and the robot's gripper is open"):
        robot.grasp("the dial")
    if check("the robot's gripper is around the dial"):
        robot.twist("the dial to the desired position")