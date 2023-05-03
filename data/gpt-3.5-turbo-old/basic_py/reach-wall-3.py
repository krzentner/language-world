if check("the robot's gripper is not near reach target and there is a wall blocking the direct path to the target"):
        robot.move("to the side of the wall")
        robot.move("to the other side of the wall")
        robot.reach("to the goal")