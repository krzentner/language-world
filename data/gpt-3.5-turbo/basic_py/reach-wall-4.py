If check("the robot's gripper is not near the wall"):
        robot.move("to the side of the wall")
    if check("the robot's gripper is near the wall"):
        robot.lift("the gripper over the wall")
    if check("the robot's gripper is above the wall and not yet at the target location"):
        robot.move("to the goal position")
    if check("the robot's gripper is at the goal position"):
        robot.lower("the gripper to the target location")