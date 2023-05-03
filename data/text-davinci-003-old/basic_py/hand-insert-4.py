
    if check("the robot's gripper is not above the puck"):
        robot.reach("gripper above puck")
    if check("the robot's gripper is not around the puck"): 
        robot.pick("puck")
    if check("the robot's gripper is near the puck and the puck is not at the goal location"):
        robot.move("puck to goal")
    if check("the puck is at the goal location"):
        robot.place("puck in target")