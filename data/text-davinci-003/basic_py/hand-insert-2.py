
    if check("the robot's gripper is not horizontally aligned with the puck and the robot's gripper is open"):
        robot.put("gripper above the puck")
    if check("the robot's gripper is vertically aligned to the puck and the robot's gripper is open"):
        robot.drop("gripper around the puck")
    if check("the robot's gripper is forward aligned with the puck and the robot's gripper is closed"):
        robot.lock("gripper around the puck")
    if check("the robot's gripper is downwards aligned with the puck and the robot's gripper is closed"):
        robot.grab("puck and move goal")