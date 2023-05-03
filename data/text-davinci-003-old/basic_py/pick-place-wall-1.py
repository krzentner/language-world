
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper and there is a wall in the way"):
        robot.align("gripper so the robot's arm won't hit the wall")
    if check("the robot's arm is free from the wall and the robot's gripper is closed"):
        robot.place("puck at target")