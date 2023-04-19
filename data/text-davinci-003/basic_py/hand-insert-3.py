
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is above the puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is closed"):
        robot.move("puck to goal")
    if check("the robot's gripper is at the goal location and the robot's gripper is closed"):
        robot.open("gripper to release puck at target location")