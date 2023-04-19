if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.push("gripper into puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper and there is a wall in the way"):
        robot.move("gripper to side of wall")
        robot.slide("puck around the wall")
    elif check("the robot's gripper is near the puck and the puck is below the robot's gripper and there is no wall in the way"):
        robot.slide("puck to goal")