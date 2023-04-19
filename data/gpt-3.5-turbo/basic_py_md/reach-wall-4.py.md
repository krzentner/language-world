# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    if check("the robot's gripper is not near reach target and there is a wall in the way"):
        robot.move("gripper to the left or right of the wall")
        robot.move("gripper over the wall")
        robot.reach("to goal")