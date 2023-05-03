if check("the robot's gripper is not near reach target"):
        if check("the wall is to the right of the robot's gripper"):
            robot.move("gripper to left of wall")
            robot.reach("to goal")
        elif check("the wall is to the left of the robot's gripper"):
            robot.move("gripper to right of wall")
            robot.reach("to goal")