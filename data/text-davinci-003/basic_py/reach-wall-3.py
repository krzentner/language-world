
    if check("the robot's gripper is not near reach target and the robot’s gripper is not above wall"):
        robot.put("gripper above wall")
    if check("the robot's gripper is not close to reach target and the robot's gripper is above wall"):
        robot.place("gripper in wall's way")
    if check("the robot's gripper is close to reach target and the robot's gripper is not close to reach target"):
        robot.move("gripper around wall to goal")