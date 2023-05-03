
    if check("the robot's gripper is not above the wall"):
        robot.reach("above wall")
    if check("the robot's gripper is above the wall and the robot's gripper is not close to the wall"):
        robot.reach("close to the wall")
    if check("the robot's gripper is near the wall and the target is not close to the robot's gripper"):
        robot.reach("towards target")
    if check("the target is close to the robot's gripper"):
        robot.reach("to target")