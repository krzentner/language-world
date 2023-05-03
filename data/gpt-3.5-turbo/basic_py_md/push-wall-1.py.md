# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    if check("the robot's gripper is not near puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed and there is a wall between the puck and goal"):
        robot.push("puck against wall")
    if check("the robot's gripper is near the wall and the wall is between the robot's gripper and goal"):
        robot.slide("gripper over wall")
    if check("the robot's gripper is above the puck and the puck is past the wall and the robot's gripper is closed"):
        robot.slide("puck to goal")