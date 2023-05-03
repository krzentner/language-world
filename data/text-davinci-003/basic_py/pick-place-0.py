
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.grab("the puck")
    if check("the robot's grip is around the puck and the robot's gripper is not near goal"):
        robot.move("the gripper to the goal")
    if check("the robot's gripper is near goal"):
        robot.release("puck at goal")