if check("the robot's gripper is not vertically aligned with the reach target and the robot's gripper is not above the wall"):
        robot.move("gripper above the wall")
    if check("the robot's gripper is above the wall and not near the reach target"):
        robot.move("gripper towards reach target")
    if check("the robot's gripper is near the reach target"):
        robot.reach("to goal")