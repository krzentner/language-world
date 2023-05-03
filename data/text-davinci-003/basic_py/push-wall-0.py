
    if check("the robot's gripper is not above puck and the robot's gripper is not forward aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is forward aligned with the puck and the robot's gripper is not close enough to puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is close enough to the puck and the robot's gripper is near the wall"):
        robot.push("the wall in order to slide the puck to the goal")
    if check("the robot's gripper is close enough to the puck and the wall is not in the way"):
        robot.slide("the puck to the goal")