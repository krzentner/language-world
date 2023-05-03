
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the wall"):
        robot.put("gripper near the wall")
    if check("the robot's gripper is near the wall and the robot's gripper is above the puck"):
        robot.place("puck at goal")