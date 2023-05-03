

If check("the robot's gripper is not above the puck"):
    robot.put("gripper above puck")
If check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.grab("puck")
If check("the robot's gripper is closed and the puck is not at the target location"):
    robot.move("puck to goal")
If check("the robot's gripper is closed and the puck is at the target location"):
    robot.release("puck at goal")