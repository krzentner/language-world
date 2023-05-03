
    if check("the robot's gripper is not near the puck and the robot's gripper is below the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is near the puck and the robot's gripper is not around the puck"):
        robot.put("the gripper around the puck")
    if check("the robot's gripper is around the puck and the puck is not near the goal"):
        robot.move("the puck to the goal")
    if check("the robot's gripper is around the puck and the puck is near the goal"):
        robot.release("the puck at the goal")