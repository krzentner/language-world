if check("the robot's gripper is not near the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not holding the puck"):
        robot.grab("the puck")
    if check("the robot's gripper is holding the puck and the robot's gripper is not vertically aligned with the goal"):
        robot.move("the gripper to the goal location")
    if check("the robot's gripper is near the goal and the puck is below the robot's gripper"):
        robot.release("the puck at the goal location")