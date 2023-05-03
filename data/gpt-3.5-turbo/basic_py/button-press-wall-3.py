if check("the robot's gripper is not near the wall and the robot's gripper is not vertically aligned with button"):
        robot.move("gripper to wall")
    if check("the robot's gripper is near the wall and the robot's gripper is not vertically aligned with button"):
        robot.lift("gripper up")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button with gripper")