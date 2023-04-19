if check("the robot's gripper is not near reach target"):
    if check("there is a short wall blocking the path to the reach target"):
        robot.lift("the gripper over the wall")
    robot.reach("to goal")