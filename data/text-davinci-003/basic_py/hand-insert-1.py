
    if check("the robot's gripper is not above the puck and the robot's gripper is not forward aligned with the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is forward aligned with puck"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is forward aligned with the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is forward aligned with the puck and the robot's gripper is closed"):
        robot.move("puck to goal")