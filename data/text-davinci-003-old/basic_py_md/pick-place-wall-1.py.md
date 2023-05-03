

If check("the robot's gripper is not almost vertically aligned with the wall"):
    robot.put("gripper above wall")
if check("the robot's gripper is almost vertically aligned with the wall and the robot's gripper is not near the wall"):
    robot.put("gripper in front of wall")
if check("the robot's gripper is near the wall and the robot's gripper is open"):
    robot.grab("wall and move it over the puck")
if check("the robot's gripper is in front of the wall and the puck is below the robot's gripper"):
    robot.grab("puck")
if check("the robot's gripper is near the puck and the robot's gripper is open"):
    robot.close("gripper around puck")
if check("the robot's gripper is above puck and the robot's gripper is closed"):
    robot.place("puck at goal")