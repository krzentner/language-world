# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
def reach_wall(robot):
    if check("the robot's gripper is not near the wall"):
        robot.move("gripper to wall")
    if check("the robot's gripper is near the wall"):
        robot.slide("gripper along the wall to the target location")