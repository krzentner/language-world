if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck"):
        robot.grab("puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move("puck to goal")
    if check("the robot's gripper is above goal"):
        robot.release("puck")