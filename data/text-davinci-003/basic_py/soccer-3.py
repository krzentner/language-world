
    if check("the robot's gripper is not above the ball"):
        robot.put("gripper above ball")
    if check("the robot's gripper is above theball and the robot's gripper is not around ball"):
        robot.grab("ball")
    if check("the robot's gripper is around the ball and the robot is not aligned with the goal"):
        robot.align("robot to goal")
    if check("the robot is aligned with goal"):
        robot.push("ball to goal")