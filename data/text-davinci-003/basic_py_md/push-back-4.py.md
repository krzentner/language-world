

if check("the robot's gripper is not near the puck"):
    robot.move("gripper near puck")
if check("the robot's gripper is near the puck and the robot's gripper is vertically aligned with the puck"):
    robot.push("gripper away from the puck")
if check("the robot's gripper is in front of the puck"):
    robot.slide("puck backwards")