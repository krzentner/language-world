if check("the robot's gripper is not above the puck"):
    robot.place("gripper above puck")
if check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.drop("gripper around puck")
if check("the robot's gripper is near puck and the robot's gripper is open"):
    robot.close("gripper around puck")
if check("the robot's gripper is clear of the short wall"):
    robot.move("gripper over the wall")
if check("the robot's gripper is near the goal and the robot's gripper is closed"):
    robot.place("puck at goal")