# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    # Steps:
    #  1. Move gripper to the side of the wall
    #  2. Move gripper towards goal
    # We need to move the gripper to the side of the wall to avoid it, then
    # move towards the goal.
    if check("the robot's gripper is not near the goal"):
        if check("the robot's gripper is to the left of the wall"):
            robot.move("gripper to right of wall")
        else:
            robot.move("gripper to left of wall")
        robot.reach("to goal")