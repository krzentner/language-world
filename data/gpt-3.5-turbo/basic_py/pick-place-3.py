if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is open and vertically aligned with the puck"):
        robot.grab("puck")
    if check("the robot's gripper is holding the puck and not vertically aligned with the goal"):
        robot.align("puck to goal")
    if check("the robot's gripper is holding the puck and vertically aligned with the goal"):
        robot.release("puck at goal")