# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    if check("the robot's gripper is not near the wall and the wall is between the robot's gripper and the goal"):
        robot.move("gripper towards wall")
    if check("the robot's gripper is near the wall and the wall is between the robot's gripper and the goal"):
        robot.lift("gripper over the wall")
    if check("the robot's gripper is over the wall and the robot's gripper is not aligned with the goal"):
        robot.move("gripper towards goal")
    if check("the robot's gripper is aligned with the goal"):
        robot.reach("to the goal")