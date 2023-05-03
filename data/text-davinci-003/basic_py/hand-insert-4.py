
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around puck"):
        robot.move("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is not near goal"):
        robot.move("puck to goal")
    if check("the robot's gripper is near the goal and the robot's gripper is open"):
        robot.release("puck at goal")