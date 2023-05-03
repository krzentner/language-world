If check("the robot's gripper is not near reach target"):
        if check("there is a short wall in front of the robot"):
            robot.lift("the gripper over the wall")
        robot.reach("to goal")