# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    if check("the robot's gripper is not aligned with the wall"):
        robot.put("gripper to side of wall")
    if check("the robot's gripper is aligned with the wall"):
        robot.move("gripper up and over wall")
    if check("the robot's gripper is on the other side of the wall and not at the target location"):
        robot.move("gripper to goal location")