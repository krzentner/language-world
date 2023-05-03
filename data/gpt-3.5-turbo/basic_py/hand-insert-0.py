    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.grab("puck")
    if check("the robot's gripper is above puck and the robot is not at the goal location"):
        robot.move("to goal location")
    if check("the robot is at the goal location"):
        robot.release("puck")